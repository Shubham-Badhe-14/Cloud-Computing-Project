'use client';

export default function Controls({ isActive, toggleTimer, resetTimer, showSettings }) {
  return (
    <div className="flex justify-center space-x-4">
      <button
        onClick={toggleTimer}
        className={`px-6 py-3 rounded-lg font-bold text-white ${
          isActive ? 'bg-blue-700 hover:bg-blue-800' : 'bg-blue-600 hover:bg-blue-700'
        }`}
      >
        {isActive ? 'Pause' : 'Start'}
      </button>
      <button
        onClick={resetTimer}
        className="px-6 py-3 rounded-lg font-bold bg-blue-500 hover:bg-blue-600 text-white"
      >
        Reset
      </button>
      <button
        onClick={showSettings}
        className="px-6 py-3 rounded-lg font-bold bg-blue-400 hover:bg-blue-500 text-white"
      >
        Settings
      </button>
    </div>
  );
}