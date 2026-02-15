import React, { useState } from 'react';
import './styles.css';

const ChapterControls: React.FC = () => {
  const [showToast, setShowToast] = useState(false);
  const [toastMsg, setToastMsg] = useState('');

  const handlePersonalize = () => {
    setToastMsg('🤖 Customizing content for your background: System Engineer (Focus: Humanoids)...');
    setShowToast(true);
    setTimeout(() => setShowToast(false), 3000);
  };

  const handleTranslate = () => {
    setToastMsg('🇵🇰 اردو ترجمہ جلد آرہا ہے! (Urdu translation coming soon!)');
    setShowToast(true);
    setTimeout(() => setShowToast(false), 3000);
  };

  return (
    <div className="chapter-controls">
      <button className="control-btn" onClick={handlePersonalize}>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
        </svg>
        Personalize Content
      </button>
      
      <button className="control-btn urdu" onClick={handleTranslate}>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M4 11v8a1 1 0 001 1h3m10-10a1 1 0 00-1-1h-3m-2 2h5m-5 3c0 1.5-1 3-3 3" />
        </svg>
        اردو ترجمہ (Urdu)
      </button>

      {showToast && (
        <div className="personalization-toast">
          {toastMsg}
        </div>
      )}
    </div>
  );
};

export default ChapterControls;
