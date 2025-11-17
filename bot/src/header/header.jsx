
import PropTypes from 'prop-types';
import './header.css'; 

const ChatHeader = ({ onMinimize }) => {
  return (
    <div className="chat-header">
      <div className="minimize-button" onClick={onMinimize}></div>
    </div>
  );
}

ChatHeader.propTypes = {
  onMinimize: PropTypes.func.isRequired,
};

export default ChatHeader;