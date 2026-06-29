<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>Samsung 2008 · TRUE Startup Sound (Your MP3)</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            background: radial-gradient(circle at 30% 20%, #0c1419, #020406);
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', system-ui, monospace;
            padding: 1.2rem;
        }

        .tv-cabinet {
            max-width: 860px;
            width: 100%;
            filter: drop-shadow(0 20px 30px rgba(0,0,0,0.7));
        }
        .bezel {
            background: #14181c;
            border-radius: 44px;
            padding: 20px 22px 26px 22px;
            box-shadow: inset 0 1px 2px rgba(255,255,255,0.06), 0 12px 28px black;
            border: 1px solid #2e3a40;
        }
        .screen {
            background: #01070a;
            border-radius: 32px;
            padding: 2rem 1.8rem;
            position: relative;
            text-align: center;
        }
        .samsung-word {
            font-size: 2.6rem;
            font-weight: 800;
            letter-spacing: 2px;
            background: linear-gradient(145deg, #f0fcff, #9bc7e0);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .year-badge {
            font-size: 0.7rem;
            color: #468290;
            margin-top: 4px;
        }
        .display-panel {
            background: #021016;
            border-radius: 32px;
            padding: 1.8rem;
            margin: 1.2rem 0;
            border: 1px solid #1d5a66;
        }
        .control-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin: 24px 0 16px;
        }
        .tv-btn {
            background: #1f2e34;
            border: none;
            padding: 12px 28px;
            border-radius: 80px;
            font-weight: bold;
            font-size: 0.95rem;
            color: #eef7fc;
            cursor: pointer;
            transition: 0.12s linear;
            border-bottom: 2px solid #378c9b;
            font-family: inherit;
        }
        .tv-btn:active {
            transform: scale(0.96);
        }
        .volume-slider {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            margin: 16px 0;
        }
        .footer-note {
            font-size: 0.68rem;
            color: #316d7a;
            text-align: center;
            border-top: 1px solid #1d4b55;
            padding-top: 16px;
            margin-top: 10px;
        }
        .status {
            font-family: monospace;
            font-size: 0.8rem;
            color: #70bacb;
            margin-top: 12px;
        }
        .file-hint {
            background: #1a2a2a;
            border-radius: 20px;
            padding: 8px;
            margin-top: 12px;
            font-size: 0.7rem;
            color: #88bbaa;
        }
        .error-msg {
            color: #ff8866;
        }
    </style>
</head>
<body>
<div class="tv-cabinet">
    <div class="bezel">
        <div class="screen">
            <div class="samsung-word">SAMSUNG</div>
            <div class="year-badge">◤ 2008 DIGITAL VISION ◢</div>
            <div class="display-panel">
                <div style="font-size: 5rem; margin: 20px 0;">📺</div>
                <div class="status" id="statusMsg">⚡ READY · CLICK POWER</div>
            </div>
            <div class="control-buttons">
                <button class="tv-btn" id="powerBtn">⏻ POWER ON · STARTUP</button>
                <button class="tv-btn" id="replayBtn">🎵 REPLAY STARTUP SOUND</button>
            </div>
            <div class="volume-slider">
                <span>🔊</span>
                <input type="range" id="volume" min="0" max="1" step="0.01" value="0.8">
                <span id="volPercent">80%</span>
            </div>
            <div class="footer-note">
                🎼 <strong>AUTHENTIC 2008 Samsung startup sound</strong> — from your MP3 file<br>
                📺 Original YouTube source: AOGdwgNrtZY · NOT a chime · full arpeggio
            </div>
            <div class="file-hint" id="fileHint">
                📁 Using your local file: <strong id="fileName">Samsung TV Startup & Shutdown High Quality 2000s-2010s.mp3</strong>
            </div>
        </div>
    </div>
</div>

<script>
    (function() {
        // ============================================================
        // USING YOUR LOCAL MP3 FILE
        // File path: C:/Users/Sam%20Arnaiz/Downloads/Samsung%20TV%20Startup%20&%20Shutdown%20High%20Quality%202000s-2010s.mp3
        // ============================================================
        
        let currentVolume = 0.8;
        let isPlaying = false;
        let currentAudio = null;
        
        // Create audio element with your local file
        const audioPlayer = new Audio();
        // Use the exact file path (URL encoded spaces are fine, but we set src properly)
        const mp3Path = "C:/Users/Sam%20Arnaiz/Downloads/Samsung%20TV%20Startup%20&%20Shutdown%20High%20Quality%202000s-2010s.mp3";
        audioPlayer.src = mp3Path;
        audioPlayer.preload = "auto";
        audioPlayer.volume = currentVolume;
        
        // DOM elements
        const volumeSlider = document.getElementById('volume');
        const volSpan = document.getElementById('volPercent');
        const statusMsg = document.getElementById('statusMsg');
        const powerBtn = document.getElementById('powerBtn');
        const replayBtn = document.getElementById('replayBtn');
        const fileNameSpan = document.getElementById('fileName');
        
        // Update volume display and actual audio volume
        volumeSlider.addEventListener('input', (e) => {
            currentVolume = parseFloat(e.target.value);
            volSpan.innerText = Math.round(currentVolume * 100) + '%';
            if (audioPlayer) {
                audioPlayer.volume = currentVolume;
            }
        });
        
        // Set initial volume
        audioPlayer.volume = currentVolume;
        
        // Function to stop any currently playing audio
        function stopCurrentAudio() {
            if (currentAudio) {
                try {
                    currentAudio.pause();
                    currentAudio.currentTime = 0;
                } catch(e) { console.warn(e); }
            }
            if (audioPlayer) {
                try {
                    audioPlayer.pause();
                    audioPlayer.currentTime = 0;
                } catch(e) { console.warn(e); }
            }
        }
        
        // Play the startup sound (uses your MP3)
        async function playStartupSound() {
            if (isPlaying) {
                // If already playing, stop and restart?
                stopCurrentAudio();
                isPlaying = false;
            }
            
            try {
                // Reset audio to beginning
                audioPlayer.currentTime = 0;
                
                // Create a promise to handle play() async
                const playPromise = audioPlayer.play();
                
                if (playPromise !== undefined) {
                    await playPromise;
                    isPlaying = true;
                    return true;
                }
                return false;
            } catch (err) {
                console.error("Audio playback error:", err);
                // Check if it's a file not found error
                if (err.name === 'NotSupportedError' || err.message.includes('failed to load')) {
                    statusMsg.innerHTML = '❌ MP3 FILE NOT FOUND! Check file path.';
                } else if (err.name === 'NotAllowedError') {
                    statusMsg.innerHTML = '⚠️ Click again to enable audio (browser policy)';
                } else {
                    statusMsg.innerHTML = '⚠️ Error playing: ' + err.message.substring(0, 50);
                }
                isPlaying = false;
                return false;
            }
        }
        
        // Handle audio end event
        audioPlayer.addEventListener('ended', () => {
            isPlaying = false;
            // Don't auto-change status message if user just replayed
            if (statusMsg.innerHTML.includes('PLAYING')) {
                statusMsg.innerHTML = '✅ STARTUP COMPLETE · SAMSUNG READY';
                setTimeout(() => {
                    if (statusMsg.innerHTML.includes('COMPLETE')) {
                        statusMsg.innerHTML = '⚡ POWER ON · SAMSUNG';
                    }
                }, 1800);
            }
        });
        
        // Handle audio errors
        audioPlayer.addEventListener('error', (e) => {
            console.error("Audio error event:", e);
            let errorMsg = "❌ Cannot load MP3 file.";
            if (audioPlayer.error) {
                switch(audioPlayer.error.code) {
                    case 1: errorMsg = "❌ MP3 loading aborted."; break;
                    case 2: errorMsg = "❌ Network error - file not found at that path."; break;
                    case 3: errorMsg = "❌ Decoding error - file may be corrupted."; break;
                    case 4: errorMsg = "❌ Format not supported."; break;
                }
            }
            statusMsg.innerHTML = errorMsg + " Check file location.";
            isPlaying = false;
        });
        
        // Full power-on sequence with visual feedback
        async function powerOnSequence() {
            // Stop any existing playback
            stopCurrentAudio();
            isPlaying = false;
            
            statusMsg.innerHTML = '🔊 PLAYING STARTUP SOUND...';
            
            // Small delay to ensure UI updates
            await new Promise(r => setTimeout(r, 50));
            
            const played = await playStartupSound();
            
            if (played) {
                statusMsg.innerHTML = '✅ SAMSUNG 2008 · SYSTEM BOOTING';
                // Don't override the 'ended' event message, but set fallback
                setTimeout(() => {
                    if (statusMsg.innerHTML.includes('BOOTING') && !isPlaying) {
                        statusMsg.innerHTML = '✅ SAMSUNG 2008 · SYSTEM READY';
                        setTimeout(() => {
                            if (statusMsg.innerHTML.includes('READY')) {
                                statusMsg.innerHTML = '⚡ POWER ON · SAMSUNG';
                            }
                        }, 1500);
                    }
                }, 2000);
            } else if (!statusMsg.innerHTML.includes('NOT FOUND') && !statusMsg.innerHTML.includes('error')) {
                statusMsg.innerHTML = '⚠️ Click again to enable audio (browser requires interaction)';
            }
        }
        
        // Replay only the sound with minimal visual feedback
        async function replaySound() {
            stopCurrentAudio();
            isPlaying = false;
            
            statusMsg.innerHTML = '🎵 REPLAYING STARTUP MELODY...';
            
            await new Promise(r => setTimeout(r, 30));
            
            const played = await playStartupSound();
            
            if (!played && !statusMsg.innerHTML.includes('NOT FOUND')) {
                if (!statusMsg.innerHTML.includes('error')) {
                    statusMsg.innerHTML = '⚠️ Click POWER ON first to enable audio';
                }
            } else if (played) {
                // Success message will be updated by 'ended' event
                setTimeout(() => {
                    if (statusMsg.innerHTML.includes('REPLAYING')) {
                        statusMsg.innerHTML = '🎵 SOUND PLAYING';
                    }
                }, 100);
            }
        }
        
        // Preload audio metadata to check if file exists
        async function checkAudioFile() {
            return new Promise((resolve) => {
                const testAudio = new Audio();
                testAudio.src = mp3Path;
                testAudio.addEventListener('canplaythrough', () => {
                    resolve(true);
                    testAudio.src = '';
                });
                testAudio.addEventListener('error', () => {
                    resolve(false);
                    testAudio.src = '';
                });
                // Timeout after 2 seconds
                setTimeout(() => resolve(false), 2000);
            });
        }
        
        // Check if file exists on page load and show status
        async function init() {
            // Display the file name (truncated if needed)
            const fullName = "Samsung TV Startup & Shutdown High Quality 2000s-2010s.mp3";
            if (fileNameSpan) fileNameSpan.innerText = fullName;
            
            // Check if file can be loaded
            const fileExists = await checkAudioFile();
            if (fileExists) {
                statusMsg.innerHTML = '✅ MP3 loaded · READY · CLICK POWER';
                // Preload the audio
                audioPlayer.load();
            } else {
                statusMsg.innerHTML = '⚠️ MP3 not found at: Downloads folder. Make sure file exists.';
                const hintDiv = document.querySelector('.file-hint');
                if (hintDiv) {
                    hintDiv.style.background = '#3a2a2a';
                    hintDiv.innerHTML = '❌ FILE NOT FOUND!<br>Place the MP3 in: <strong>C:/Users/Sam Arnaiz/Downloads/</strong><br>Filename: <strong>Samsung TV Startup & Shutdown High Quality 2000s-2010s.mp3</strong>';
                }
            }
        }
        
        // Set up button event listeners
        powerBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            await powerOnSequence();
        });
        
        replayBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            await replaySound();
        });
        
        // Also handle any click on document to help with autoplay policies? 
        // Buttons already handle user interaction.
        
        // Initialize on load
        init();
    })();
</script>
</body>
</html>
