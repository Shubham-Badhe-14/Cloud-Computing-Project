'use client';

export default function Timer({ minutes, seconds, isWorkSession }) {
  return (
    <div className="text-center">
      <div className="text-6xl font-mono font-bold text-black"> {/* Changed to black */}
        {minutes.toString().padStart(2, '0')}:{seconds.toString().padStart(2, '0')}
      </div>
      <div className={`mt-2 text-sm font-semibold ${
        isWorkSession ? 'text-gray-800' : 'text-gray-600' // Darker black for work, lighter for break
      }`}>
        {isWorkSession ? 'FOCUS SESSION' : 'BREAK TIME'}
      </div>
    </div>
  );
}