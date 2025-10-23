import React from 'react';
import { Message } from '../types';
import { User, Bot } from 'lucide-react';
import { clsx } from 'clsx';

interface MessageBubbleProps {
  message: Message;
}

export const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const isUser = message.sender === 'user';
  const isAi = message.sender === 'ai';

  return (
    <div
      className={clsx(
        'flex gap-3 p-4 animate-slide-up',
        isUser ? 'justify-end' : 'justify-start'
      )}
    >
      {isAi && (
        <div className="flex-shrink-0">
          <div className="w-8 h-8 rounded-full bg-primary-500 flex items-center justify-center">
            <Bot size={16} className="text-white" />
          </div>
        </div>
      )}
      
      <div
        className={clsx(
          'max-w-[80%] rounded-2xl px-4 py-3 shadow-sm',
          isUser
            ? 'bg-primary-500 text-white rounded-br-sm'
            : 'bg-gray-100 text-gray-900 rounded-bl-sm'
        )}
      >
        <p className="text-sm whitespace-pre-wrap leading-relaxed">
          {message.content}
        </p>
        <p className={clsx(
          'text-xs mt-2 opacity-70',
          isUser ? 'text-primary-100' : 'text-gray-500'
        )}>
          {message.timestamp.toLocaleTimeString([], { 
            hour: '2-digit', 
            minute: '2-digit' 
          })}
        </p>
      </div>

      {isUser && (
        <div className="flex-shrink-0">
          <div className="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center">
            <User size={16} className="text-gray-600" />
          </div>
        </div>
      )}
    </div>
  );
};