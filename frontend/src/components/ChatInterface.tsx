import React, { useState, useRef, useEffect } from 'react';
import { Send, RotateCcw, Loader2 } from 'lucide-react';
import { useChat } from '../hooks/useChat';
import { MessageBubble } from './MessageBubble';
import { QuestionSuggestions } from './QuestionSuggestions';

export const ChatInterface: React.FC = () => {
  const { messages, isLoading, sendMessage, clearMessages } = useChat();
  const [inputValue, setInputValue] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputValue.trim() && !isLoading) {
      sendMessage(inputValue);
      setInputValue('');
    }
  };

  const handleSuggestionClick = (question: string) => {
    sendMessage(question);
  };

  const handleClearChat = () => {
    clearMessages();
    inputRef.current?.focus();
  };

  return (
    <div className="flex flex-col h-screen bg-white">
      {/* Header */}
      <div className="flex-shrink-0 bg-primary-600 text-white p-4 shadow-sm">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-xl font-semibold">Chat with Prosper's CV</h1>
            <p className="text-primary-100 text-sm">
              Ask me about my experience, skills, projects, and background
            </p>
          </div>
          <button
            onClick={handleClearChat}
            className="p-2 hover:bg-primary-500 rounded-lg transition-colors"
            title="Clear conversation"
          >
            <RotateCcw size={20} />
          </button>
        </div>
      </div>

      {/* Messages Container */}
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-4xl mx-auto">
          {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
          ))}
          
          {isLoading && (
            <div className="flex items-center gap-3 p-4">
              <div className="w-8 h-8 rounded-full bg-primary-500 flex items-center justify-center">
                <Loader2 size={16} className="text-white animate-spin" />
              </div>
              <div className="bg-gray-100 rounded-2xl rounded-bl-sm px-4 py-3">
                <p className="text-sm text-gray-600">Thinking...</p>
              </div>
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Question Suggestions */}
      <QuestionSuggestions 
        onSelectQuestion={handleSuggestionClick}
        disabled={isLoading}
      />

      {/* Input Form */}
      <div className="flex-shrink-0 border-t border-gray-200 bg-white p-4">
        <form onSubmit={handleSubmit} className="max-w-4xl mx-auto">
          <div className="flex gap-3">
            <input
              ref={inputRef}
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Ask me anything about Prosper's background..."
              className="flex-1 px-4 py-3 border border-gray-300 rounded-full
                       focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent
                       disabled:opacity-50 disabled:cursor-not-allowed"
              disabled={isLoading}
            />
            <button
              type="submit"
              disabled={!inputValue.trim() || isLoading}
              className="px-6 py-3 bg-primary-500 text-white rounded-full
                       hover:bg-primary-600 disabled:opacity-50 disabled:cursor-not-allowed
                       focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2
                       transition-colors flex items-center gap-2"
            >
              {isLoading ? (
                <Loader2 size={20} className="animate-spin" />
              ) : (
                <Send size={20} />
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};