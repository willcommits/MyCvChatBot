import React, { useState, useEffect } from 'react';
import { chatAPI } from '../services/api';
import { MessageCircle } from 'lucide-react';

interface QuestionSuggestionsProps {
  onSelectQuestion: (question: string) => void;
  disabled?: boolean;
}

export const QuestionSuggestions: React.FC<QuestionSuggestionsProps> = ({ 
  onSelectQuestion, 
  disabled = false 
}) => {
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [isVisible, setIsVisible] = useState(true);

  useEffect(() => {
    const loadSuggestions = async () => {
      try {
        const response = await chatAPI.getSuggestions();
        setSuggestions(response.questions);
      } catch (error) {
        console.error('Error loading suggestions:', error);
      }
    };

    loadSuggestions();
  }, []);

  const handleQuestionClick = (question: string) => {
    onSelectQuestion(question);
    setIsVisible(false);
    // Show suggestions again after 3 seconds
    setTimeout(() => setIsVisible(true), 3000);
  };

  if (!isVisible || suggestions.length === 0) return null;

  return (
    <div className="p-4 border-t border-gray-200 bg-gray-50">
      <div className="flex items-center gap-2 mb-3">
        <MessageCircle size={16} className="text-primary-500" />
        <span className="text-sm font-medium text-gray-700">
          Suggested Questions:
        </span>
      </div>
      
      <div className="flex flex-wrap gap-2">
        {suggestions.slice(0, 4).map((question, index) => (
          <button
            key={index}
            onClick={() => handleQuestionClick(question)}
            disabled={disabled}
            className="px-3 py-2 text-xs bg-white border border-gray-200 rounded-full
                     hover:border-primary-300 hover:bg-primary-50 transition-colors
                     disabled:opacity-50 disabled:cursor-not-allowed
                     focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-1"
          >
            {question}
          </button>
        ))}
      </div>
      
      <button
        onClick={() => setIsVisible(false)}
        className="text-xs text-gray-400 hover:text-gray-600 mt-2 underline"
      >
        Hide suggestions
      </button>
    </div>
  );
};