'use client';
import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import Timer from './components/Timer';
import Controls from './components/Controls';
import Settings from './components/Settings';

export default function PomodoroTracker() {
  // State
  const [minutes, setMinutes] = useState(25);
  const [seconds, setSeconds] = useState(0);
  const [isActive, setIsActive] = useState(false);
  const [isWorkSession, setIsWorkSession] = useState(true);
  const [workDuration, setWorkDuration] = useState(25);
  const [breakDuration, setBreakDuration] = useState(5);
  const [showSettings, setShowSettings] = useState(false);

  // Timer logic
  useEffect(() => {
    let interval;
    
    if (isActive) {
      interval = setInterval(() => {
        if (seconds === 0) {
          if (minutes === 0) {
            // Switch sessions
            setIsWorkSession(!isWorkSession);
            setMinutes(isWorkSession ? breakDuration : workDuration);
            setIsActive(false);
          } else {
            setMinutes(minutes - 1);
            setSeconds(59);
          }
        } else {
          setSeconds(seconds - 1);
        }
      }, 1000);
    }

    return () => clearInterval(interval);
  }, [isActive, minutes, seconds, isWorkSession, workDuration, breakDuration]);

  const toggleTimer = () => setIsActive(!isActive);

  const resetTimer = () => {
    setIsActive(false);
    setMinutes(isWorkSession ? workDuration : breakDuration);
    setSeconds(0);
  };

  const handleSettings = (work, breakTime) => {
    setWorkDuration(work);
    setBreakDuration(breakTime);
    setMinutes(isWorkSession ? work : breakTime);
    setSeconds(0);
    setShowSettings(false);
  };

  return (
    <div className="min-h-screen bg-blue-50 flex flex-col items-center justify-center p-4"> {/* Changed to blue background */}
      <div className="text-center mb-6"> {/* Added container for instructions */}
        <h1 className="text-3xl font-bold text-blue-800 mb-2">Pomodoro Tracker</h1> {/* Blue text */}
        <p className="text-blue-600">1. Focus during work sessions (25 mins)</p> {/* Instruction line 1 */}
        <p className="text-blue-600">2. Take short breaks (5 mins) between sessions</p> {/* Instruction line 2 */}
      </div>
      
      <div className="bg-white rounded-lg shadow-xl p-8 w-full max-w-md border-2 border-blue-200"> {/* Added blue border */}
        <AnimatePresence mode="wait">
          <motion.div
            key={isWorkSession ? 'work' : 'break'}
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 1.1 }}
            transition={{ duration: 0.3 }}
            className="mb-6"
          >
            <Timer 
              minutes={minutes} 
              seconds={seconds} 
              isWorkSession={isWorkSession}
            />
          </motion.div>
        </AnimatePresence>
        
        <Controls 
          isActive={isActive}
          toggleTimer={toggleTimer}
          resetTimer={resetTimer}
          showSettings={() => setShowSettings(true)}
        />
      </div>

      {showSettings && (
        <Settings 
          workDuration={workDuration}
          breakDuration={breakDuration}
          onSubmit={handleSettings}
          onClose={() => setShowSettings(false)}
        />
      )}
    </div>
  );
}