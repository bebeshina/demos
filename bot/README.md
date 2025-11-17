<div style="display:flex;justify-content:left;width:100%;">
<img src="logo.png" alt="Test E Car Logo" width="200"/>
</div>
<div style="width:90%;text-align:left;margin-top:210px;">


## AI Powered Test E Car Chat Bot V 1.01.24

> This documentation should enable the development of the application.

## Table of contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Architecture](#architecture)

## Introduction

- This project involves an ai-powered chatbot and focuses on the Proof of Concept. The chatbot is ment to be implemented for the Test E Car website. 
The ai-powered chatbot bubble is designed to encourage the communication between visitors of the Test E Car website and the AI powered assistant. 
The main goal of this chatbot is to engage visitors and continuously train the AI model through answering their queries in real-time. 


- **Real-time Communication:** Allows visitors of the website to communicate instantly with the bot.
- **Integration with Open AI:** Interactions via the chatbot are managed through integration with Open AI (finetuned LLM).
- **Continuous training and model improvemment:** Helps to continuously enhance the chatbot performance.

## Requirements

- **Node.js and npm:** Node.js is a JavaScript runtime and npm is the package manager for Node.js. React is a JavaScript library, and thus requires Node.js for runtime execution and npm for managing dependencies.
- **Vite.js** (https://vitejs.dev/) for the POC building



### Dependencies

Here is a list of dependencies you will need to install for this project:

To install additional libraries or dependencies for the project, you can use npm.
   ```
   npm i
   ```
#### Development Dependencies (to be completed):
- **@babel**: The Babel compiler.
- **@aashutoshrathi**: Wrap words to a specified length.
- **@ampproject**: Remapper.
- **@chatscope**: Open source UI toolkit for developing web chat applications.
- **@esbuild**: Bundler for the Web.
- **@eslint**: Fixes .js code.
- **@eslint-community**: Helps fixing .js code.
- **@fortawesome**: Icon & typeface manager.
- **@humanwhocodes**: JS utilities.
- **@jiridgewell**: allows to generate a source map during transpilation or minification. 
- **@nodelib**: JS utilities.
- **@rollup**: JS utilities.
- **@types**: JS utilities.
- **@ungap**: JS utilities.
- **@vitejs**: Local development server written by Evan You, can be used for React project templates..
- **openai**: Open AI SDK
- etc.


### Configuration

- **OAKEY**: Open AI API Key.
- **OAORG**: Open AI organization token.

To avoid embedding the Zendesk key directly in the website, a random key is used and is retrieved from a hidden input field on their site.

- **ZK1**: This key is for pre-production (to be confirmed).
- **ZK0**: This key is for production (to be confirmed).

- **THEME**: Defines the theme. Default value is 'meetdeal-normal'.
- **TAGS**: The tag of the conversation that appears in Zendesk.Default value (to be confirmed) is 'tecbot'.
- **DEPARTMENT**: The service that links the chat bubble and Zendesk.Default value is 'Test E Car Bot'.
- **BRAND**: The brand of the chat bubble.Default value is 'Test E Car'.
- **BOT_AVATAR**: The URL of the image for the first avatar that appears in the initial message.Default value is 'https://chatbot-api-media.meetdeal.video/static/avatar/Avatar-Emmau-Audi(100X100).png'.


## Usage

To eventually implement the chat on a client's website, an additional documentation will be created.


## Architecture
## Project Directory Structure

Below is the directory structure of the project:

```sh
├── index.html              # Main HTML file, entry point of the chatbot application
├── package.json            # Defines packages and scripts for the project
├── package-lock.json       # Describes the exact tree generated, to ensure repeatable installations
├── README.md               # Documentation
├── src                     # Source files
│   ├── components          # React components
│   │   ├── App.jsx        # Basic app 
│   ├── main.jsx            # Main entry point of the app

_(to be updated)_
```
