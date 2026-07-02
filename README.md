# CYBER-SCANNER 📡
A powerful termux based tool for network scanning and device discovery tool built for cyber security learning, authorised penetration testing, and network analysis.  This tool automatically scans the connected wifi network and identifies active devices, IP addresses, CCTV/IP cameras. and other  network-related information in real time. 
![Have a look👀](.//Screenshot_2026-05-24-13-26-02-261_com.termux-edit.jpg) 
```
pkg update && pkg upgrade
```

```
pkg install python
```

```
pkg install python3
```

```
cd CYBER-SCANNER
```

```
python3 CYBER-SCANNER.PY
```

```
python3 cyber-scanner-py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>BAIDAR.IR · Social Links</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #0b0d14;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', 'Segoe UI', system-ui, sans-serif;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 750px;
        }

        .card {
            background: rgba(18, 24, 40, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-radius: 40px;
            padding: 3rem 2.8rem 2.8rem;
            border: 1px solid rgba(255, 255, 255, 0.04);
            box-shadow: 0 30px 60px -20px #000000ee, 0 0 0 1px rgba(255, 255, 255, 0.02);
        }

        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 2.8rem;
        }

        .logo-area {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .logo-icon {
            width: 52px;
            height: 52px;
            background: linear-gradient(135deg, #1f2a46, #131c30);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            color: #8aa3d6;
            box-shadow: inset 0 -3px 0 #2e4060;
            border: 1px solid #3d527740;
        }

        .title-group h1 {
            font-size: 1.9rem;
            font-weight: 700;
            background: linear-gradient(to right, #f0f4ff, #b0c6f0);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            letter-spacing: -0.5px;
        }

        .title-group .sub {
            color: #6f81a8;
            font-size: 0.8rem;
            font-weight: 400;
            letter-spacing: 0.3px;
        }
        .title-group .sub i {
            color: #3b82f6;
            font-size: 0.5rem;
            margin-right: 4px;
        }

        .status-chip {
            background: rgba(59, 130, 246, 0.08);
            padding: 0.3rem 1.2rem;
            border-radius: 40px;
            border: 1px solid #3b82f630;
            color: #88aaff;
            font-size: 0.65rem;
            font-weight: 500;
            letter-spacing: 0.6px;
            text-transform: uppercase;
        }
        .status-chip i {
            margin-right: 5px;
            color: #4caf84;
        }

        .btn-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 1.2rem;
        }

        .social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.8rem;
            padding: 0.9rem 1.2rem;
            background: rgba(28, 38, 58, 0.6);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            border-radius: 60px;
            border: 1px solid rgba(255, 255, 255, 0.04);
            box-shadow: 0 6px 16px -6px #000000aa;
            color: #d6def0;
            font-weight: 500;
            font-size: 0.95rem;
            text-decoration: none;
            transition: all 0.25s cubic-bezier(0.15, 0.85, 0.35, 1.2);
            position: relative;
            cursor: pointer;
            outline: none !important;
            -webkit-tap-highlight-color: transparent !important;
            user-select: none;
        }

        .social-btn:focus,
        .social-btn:focus-visible,
        .social-btn:active {
            outline: none !important;
            box-shadow: 0 6px 16px -6px #000000aa !important;
        }

        .social-btn i {
            font-size: 1.4rem;
            width: 1.8rem;
            text-align: center;
            transition: all 0.25s ease;
        }

        .social-btn .label {
            font-weight: 500;
            transition: all 0.2s;
        }

        .social-btn:hover {
            transform: translateY(-3px) scale(1.03);
            box-shadow: 0 16px 30px -10px #000000ee, 0 0 0 1px rgba(255, 255, 255, 0.06);
        }

        .social-btn:hover i {
            transform: scale(1.15) rotate(-3deg);
        }

        .social-btn:hover .label {
            transform: translateX(2px);
        }

        .social-btn.github:hover {
            background: #1c2333;
            border-color: #8b9fc0;
            color: #ffffff;
        }
        .social-btn.github i { color: #c9d2e6; }

        .social-btn.instagram:hover {
            background: linear-gradient(145deg, #d62976, #c32aa3);
            border-color: #f77737;
            color: #fff;
        }
        .social-btn.instagram i { color: #ffe2ef; }

        .social-btn.facebook:hover {
            background: #1877f2;
            border-color: #5c94f7;
            color: #fff;
        }
        .social-btn.facebook i { color: #c2d8ff; }

        .social-btn.twitter:hover {
            background: #0f1419;
            border-color: #8a9bb0;
            color: #fff;
        }
        .social-btn.twitter i { color: #e6edf8; }

        .social-btn.whatsapp:hover {
            background: #1ebe5c;
            border-color: #6bea9a;
            color: #fff;
        }
        .social-btn.whatsapp i { color: #d4fade; }

        .social-btn:active {
            transform: scale(0.94) !important;
            transition-duration: 0.04s;
        }

        @media (max-width: 600px) {
            .card {
                padding: 2rem 1.5rem;
                border-radius: 32px;
            }
            .title-group h1 {
                font-size: 1.5rem;
            }
            .logo-icon {
                width: 44px;
                height: 44px;
                font-size: 1.3rem;
            }
            .btn-grid {
                grid-template-columns: 1fr 1fr;
                gap: 0.9rem;
            }
            .social-btn {
                padding: 0.7rem 0.8rem;
                font-size: 0.85rem;
                gap: 0.5rem;
            }
            .social-btn i {
                font-size: 1.2rem;
                width: 1.5rem;
            }
        }

        @media (max-width: 400px) {
            .btn-grid {
                grid-template-columns: 1fr;
            }
            .header {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        @keyframes slideUp {
            0% { opacity: 0; transform: translateY(16px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .social-btn {
            animation: slideUp 0.5s ease forwards;
            opacity: 0;
        }
        .social-btn:nth-child(1) { animation-delay: 0.03s; }
        .social-btn:nth-child(2) { animation-delay: 0.07s; }
        .social-btn:nth-child(3) { animation-delay: 0.11s; }
        .social-btn:nth-child(4) { animation-delay: 0.15s; }
        .social-btn:nth-child(5) { animation-delay: 0.19s; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">

            <div class="header">
                <div class="logo-area">
                    <div class="logo-icon">
                        <i class="fas fa-link"></i>
                    </div>
                    <div class="title-group">
                        <h1>BAIDAR.IR</h1>
                        <div class="sub">
                            <i class="fas fa-circle"></i> social connect
                        </div>
                    </div>
                </div>
                <div class="status-chip">
                    <i class="fas fa-check-circle"></i> 5 links
                </div>
            </div>

            <div class="btn-grid">

                <a href="https://github.com/iambaidar" target="_self" rel="noopener noreferrer" class="social-btn github">
                    <i class="fab fa-github"></i>
                    <span class="label">GitHub</span>
                </a>

                <a href="https://www.instagram.com/cyber.irr?igsh=MXVsM3RlYjBxbzVicw==" target="_self" rel="noopener noreferrer" class="social-btn instagram">
                    <i class="fab fa-instagram"></i>
                    <span class="label">Instagram</span>
                </a>

                <a href="https://www.facebook.com/share/1JbumLyrUs/" target="_self" rel="noopener noreferrer" class="social-btn facebook">
                    <i class="fab fa-facebook-f"></i>
                    <span class="label">Facebook</span>
                </a>

                <a href="https://x.com/thebaidar" target="_self" rel="noopener noreferrer" class="social-btn twitter">
                    <i class="fab fa-x-twitter"></i>
                    <span class="label">Twitter</span>
                </a>

                <a href="https://whatsapp.com/channel/0029VbBHZK35fM5TATDGil3o" target="_self" rel="noopener noreferrer" class="social-btn whatsapp">
                    <i class="fab fa-whatsapp"></i>
                    <span class="label">WhatsApp</span>
                </a>

            </div>

        </div>
    </div>

    <script>
        // Force redirect agar koi issue ho
        document.querySelectorAll('.social-btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                window.location.href = this.href;
            });
        });
    </script>
</body>
</html>
