import { useState, useEffect } from 'react'
import './App.css'
import logoImage from './assets/Triforce.webp'

const API_BASE = ''; 

function App() {
  const [activeTab, setActiveTab] = useState('audio')
  const [isConnected, setIsConnected] = useState(false)
  const [availableFiles, setAvailableFiles] = useState([]) 

  const [hwStatus, setHwStatus] = useState({
    state: 'UNKNOWN',
    gps: 'Waiting for data...',
    display: '----',
    pttKeyed: false
  })

  const [settings, setSettings] = useState({
    delay: 2.0,
    duration: 3,
    volume: 1.0,
    msg_type: 'test.wav',
    record_mode: 'retro' // This line is for toggling between 'pre and post' record
  })
  const [manualPtt, setManualPtt] = useState(false)

  useEffect(() => {
    fetch(`${API_BASE}/api/settings`)
      .then(res => res.json())
      .then(data => {
        setSettings(prev => ({ ...prev, ...data }))
        setIsConnected(true)
      })
      .catch(() => setIsConnected(false))

    fetch(`${API_BASE}/api/status`)
      .then(res => res.json())
      .then(data => setHwStatus(data))
      .catch(err => console.error("Status error:", err))
      
    fetch(`${API_BASE}/api/files`)
      .then(res => res.json())
      .then(data => setAvailableFiles(data.files || [])) 
      .catch(err => console.error("Files error:", err))
  }, [])

  // --- BUTTON ACTIONS ---
  const handleSave = async () => {
    try {
      const response = await fetch(`${API_BASE}/api/settings`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(settings)
      });
      const result = await response.json();
      alert("Success: " + result.message);
    } catch (error) {
      alert("Error: Could not save settings.");
    }
  }

  const handleShutdown = async () => {
    if (window.confirm("WARNING: Are you sure you want to shut down the Pi?")) {
      try {
        await fetch(`${API_BASE}/api/system/shutdown`, { method: 'POST' });
        alert("Shutting down... Wait 15 seconds before removing power.");
      } catch (error) {
        console.error("Shutdown failed:", error);
      }
    }
  }

  const handleManualPTT = async () => {
    const newState = !manualPtt;
    try {
      await fetch(`${API_BASE}/api/tools/ptt`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ state: newState })
      });
      setManualPtt(newState);
    } catch (error) {
      console.error("Failed to toggle PTT:", error);
      alert("Error communicating with the Pi API.");
    }
  }

  // --- MAIN UI ---
  return (
    <div className="app-container">
      <header>
        {/* Make sure the src matches the exact name of your file in the public folder! */}
        <img src={logoImage} alt="AVTX Logo" className="app-logo" />
        <h1 className="header-title">TRICORDER WEB GUI</h1>
      </header>
      
      <nav className="tab-menu" style={{ display: 'flex', gap: '5px'}}>
        <button style={{ flex: 1 }} className={activeTab === 'status' ? 'active' : ''} onClick={() => setActiveTab('status')}>Hardware</button>
        <button style={{ flex: 1 }} className={activeTab === 'audio' ? 'active' : ''} onClick={() => setActiveTab('audio')}>Audio</button>
        <button style={{ flex: 1 }} className={activeTab === 'settings' ? 'active' : ''} onClick={() => setActiveTab('settings')}>Settings</button>
        <button style={{ flex: 1 }} className={activeTab === 'tools' ? 'active' : ''} onClick={() => setActiveTab('tools')}>Tools</button>
      </nav>

      <main className="content-area">
        
        {/* --- STATUS TAB --- */}
        {activeTab === 'status' && (
          <div className="card">
            <h2>Live Hardware Status</h2>
            <div className="status-grid">
              <p><strong>API Connection:</strong> 
                <span style={{ color: isConnected ? '#00ffcc' : '#ff4444', marginLeft: '10px' }}>
                  {isConnected ? 'ONLINE' : 'OFFLINE'}
                </span>
              </p>
              <p><strong>System State:</strong> {hwStatus.state}</p>
              <p><strong>7-Seg Display:</strong> {hwStatus.display}</p>
              <p><strong>GPS Location:</strong> {hwStatus.gps}</p>
              <p><strong>Radio PTT:</strong> 
                <span style={{ color: hwStatus.pttKeyed ? '#ff4444' : '#00ffcc', marginLeft: '10px' }}>
                  {hwStatus.pttKeyed ? 'TRANSMITTING' : 'OPEN'}
                </span>
              </p>
            </div>
          </div>
        )}

        {/* --- AUDIO TAB --- */}
        {activeTab === 'audio' && (
          <div className="card">
            <h2>Audio Management</h2>
            <div className="form-group">
              <label>Selected Transmission File or Folder:</label>
              <input 
                type="text" 
                list="known-files"
                value={settings.msg_type}
                onChange={(e) => setSettings({...settings, msg_type: e.target.value})}
                placeholder="Select from list or type a custom path..."
              />
              <datalist id="known-files">
                {availableFiles.map((fileItem, index) => {
                  const path = typeof fileItem === 'string' ? fileItem : fileItem.filepath;
                  return <option key={index} value={path} />
                })}
              </datalist>
            </div>
            <div className="form-group">
              <label>System Volume ({Math.round(settings.volume * 100)}%)</label>
              <input 
                type="range" 
                min="0" max="1" step="0.01" 
                value={settings.volume}
                onChange={(e) => setSettings({...settings, volume: parseFloat(e.target.value)})}
                style={{ width: '100%', marginTop: '10px' }}
              />
            </div>
          </div>
        )}

        {/* --- SETTINGS TAB --- */}
        {activeTab === 'settings' && (
          <div className="card">
            <h2>Program Mode Configuration</h2>
            <div className="form-group">
                  <label>Hardware Record Button Behavior:</label>
                  <select 
                    value={settings.record_mode || 'retro'} 
                    onChange={(e) => setSettings({...settings, record_mode: e.target.value})}
                  >
                    <option value="retro">Dashcam Mode (Save PREVIOUS 10 Seconds)</option>
                    <option value="post">Standard Mode (Record NEXT 10 Seconds)</option>
                  </select>
                </div>
            <div className="form-group">
              <label>Transmission Delay (Seconds):</label>
              <input 
                type="number" 
                value={settings.delay} 
                onChange={(e) => setSettings({...settings, delay: parseFloat(e.target.value)})}
              />
            </div>
            <div className="form-group">
              <label>Sequence Iterations:</label>
              <input 
                type="number" 
                value={settings.duration} 
                onChange={(e) => setSettings({...settings, duration: parseInt(e.target.value)})}
              />
            </div>
            <div style={{ display: 'flex', gap: '10px', marginTop: '20px' }}>
              <button className="btn-save" onClick={handleSave} style={{ flex: 1 }}>Save Settings to Pi</button>
              <button onClick={handleShutdown} style={{ flex: 1, backgroundColor: '#ff4444', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}>
                Shutdown System
              </button>
            </div>
          </div>
        )}

        {/* --- TOOLS TAB --- */}
        {activeTab === 'tools' && (
          <div className="card">
            <h2>System Tools</h2>
            <div className="form-group" style={{ textAlign: 'center', marginTop: '20px' }}>
              <p style={{ color: '#aaa', marginBottom: '15px' }}>
                Use this to manually key the radio and test transmission range or hardware wiring.
              </p>
              <button 
                onClick={handleManualPTT} 
                style={{ 
                  backgroundColor: manualPtt ? '#ff4444' : '#00cc66', 
                  color: 'white', 
                  padding: '20px', 
                  fontSize: '18px', 
                  width: '100%', 
                  border: 'none', 
                  borderRadius: '8px', 
                  cursor: 'pointer',
                  fontWeight: 'bold',
                  boxShadow: manualPtt ? '0 0 15px #ff4444' : 'none'
                }}>
                {manualPtt ? 'RELEASE PTT (STOP TRANSMITTING)' : 'KEY PTT (START TRANSMITTING)'}
              </button>
            </div>
          </div>
        )}

      </main>
    </div>
  )
}

export default App