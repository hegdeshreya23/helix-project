// src/components/workspace/Workspace.tsx
import React from 'react';

interface WorkspaceProps {
  sequence: string;
}

const Workspace: React.FC<WorkspaceProps> = ({ sequence }) => {
  const formatSequence = (sequence: string) => {
    if (!sequence) return [];
    
    // Split by "Step" and filter out empty strings
    return sequence.split(/Step \d+:/)
      .filter(step => step.trim())
      .map(step => step.trim());
  };

  const steps = formatSequence(sequence);

  return (
    <div className="flex-1 flex flex-col bg-gray-50">
      <div className="p-4 border-b border-gray-200 bg-white">
        <h2 className="text-lg font-medium text-gray-900">Sequence</h2>
      </div>
      <div className="flex-1 overflow-y-auto p-4">
        {steps.length > 0 ? (
          <div className="space-y-4">
            {steps.map((step, index) => (
              <div key={index} className="bg-white rounded-lg shadow p-4">
                <div className="font-medium text-gray-900 mb-2">Step {index + 1}:</div>
                <div className="text-gray-600">{step}</div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center text-gray-500 mt-8">
            No sequence generated.
          </div>
        )}
      </div>
    </div>
  );
};

export default Workspace;