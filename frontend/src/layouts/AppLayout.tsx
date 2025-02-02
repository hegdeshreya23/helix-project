import React, { useState } from 'react';
import ChatInterface from '../components/chat/ChatInterface';
import Workspace from '../components/workspace/DynamicWork';

const AppLayout: React.FC = () => {
  const [currentSequence, setCurrentSequence] = useState<string>('');

  const handleSequenceUpdate = (sequence: string) => {
    setCurrentSequence(sequence);
  };

  return (
    <div className="flex h-screen">
      {/* Chat Interface */}
      <div className="w-1/2 border-r h-full">
        <ChatInterface onSequenceUpdate={handleSequenceUpdate} />
      </div>

      {/* Sequence Area */}
      <div className="w-1/2 h-full">
        <Workspace sequence={currentSequence} />
      </div>
    </div>
  );
};

export default AppLayout;
