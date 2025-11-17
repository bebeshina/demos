import { useState } from 'react';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator,
} from '@chatscope/chat-ui-kit-react';
import BtnClose from './../btnClose/btnClose.jsx';
import ChatHeader from './../header/header.jsx';

const API_KEY = import.meta.env.VITE_API_KEY;

import './App.css';

const App = () => {
  const [messages, setMessages] = useState([
    {
      message: 'Bonjour, je suis le bot spécialiste automobile. Posez moi des questions!',
      sentTime: 'just now',
      sender: 'LeBot',
    },
  ]);
  const [isTyping, setIsTyping] = useState(false);
  const [isMinimized, setIsMinimized] = useState(false);

  const handleMinimize = () => {
    setIsMinimized(!isMinimized);
  };

  const handleSendRequest = async (message) => {
    const newMessage = {
      message,
      direction: 'outgoing',
      sender: 'user',
    };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setIsTyping(true);

    try {
      const response = await processMessageToChatGPT([...messages, newMessage]);
      const content = response.choices[0]?.message?.content;
      if (content) {
        const chatGPTResponse = {
          message: content,
          sender: 'LeBot',
        };
        setMessages((prevMessages) => [...prevMessages, chatGPTResponse]);
      }
    } catch (error) {
      console.error('Error processing message:', error);
    } finally {
      setIsTyping(false);
    }
  };
  async function processMessageToChatGPT(chatMessages) {
    const apiMessages = chatMessages.map((messageObject) => {
      const role = messageObject.sender === 'LeBot' ? 'assistant' : 'user';
      return { role, content: messageObject.message };
    });
    const apiRequestBody = {
      model: 'gpt-3.5-turbo',
      messages: [
        { role: 'system', content: "Je suis un Ami Test, j'utilise cette IA pour apprentissage" },
        ...apiMessages,
      ],
    };
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: 'Bearer ' + API_KEY,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(apiRequestBody),
    });

    return response.json();
  }

  return (
    <div className="App">
      <h1 className="text-3xl font-bold underline">
      Test Bot
    </h1>
      <div
        style={{
          position: 'absolute',
          right: '10px',
          bottom: '10px',
          width: '370px',
          display: isMinimized ? 'block' : 'none',
        }}
      >
        <ChatHeader onMinimize={handleMinimize} />
        <MainContainer style={{ height: '422px' }}>
          <ChatContainer>
            <MessageList
              scrollBehavior="smooth"
              typingIndicator={isTyping ? <TypingIndicator content="LeBot is typing" /> : null}
            >
              {messages.map((message, i) => {
                console.log(message);
                return <Message key={i} model={message} />;
              })}
            </MessageList>
            <MessageInput id="" placeholder="Tapez votre message" onSend={handleSendRequest} />
          </ChatContainer>
        </MainContainer>
      </div>
      <div style={{ display: isMinimized ? 'none' : 'block' }} onClick={handleMinimize}>
        <BtnClose />
      </div>
    </div>
  );
};

export default App;
