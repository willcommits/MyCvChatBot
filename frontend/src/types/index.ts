export interface Message {
  id: string;
  content: string;
  sender: 'user' | 'ai';
  timestamp: Date;
}

export interface ChatSession {
  id: string;
  messages: Message[];
  createdAt: Date;
}

export interface ApiResponse {
  response: string;
  session_id: string;
}

export interface SuggestionResponse {
  questions: string[];
}