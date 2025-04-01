'use client';
import { useState } from 'react';

export default function Settings({ workDuration, breakDuration, onSubmit, onClose }) {
  const [work, setWork] = useState(workDuration);
  const [breakTime, setBreakTime] = useState(breakDuration);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(parseInt(work), parseInt(breakTime));
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <div className="bg-white rounded-lg p-6 w-full max-w-md mx-4">
        <h2 className="text-xl font-bold mb-4 text-gray-800">Timer Settings</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2">Work (minutes):</label>
            <input
              type="number"
              min="1"
              max="60"
              value={work}
              onChange={(e) => setWork(e.target.value)}
              className="w-full p-2 border rounded"
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 mb-2">Break (minutes):</label>
            <input
              type="number"
              min="1"
              max="30"
              value={breakTime}
              onChange={(e) => setBreakTime(e.target.value)}
              className="w-full p-2 border rounded"
            />
          </div>
          <div className="flex justify-end space-x-3">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-4 py-2 rounded-lg bg-green-500 hover:bg-green-600 text-white"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  );
} 