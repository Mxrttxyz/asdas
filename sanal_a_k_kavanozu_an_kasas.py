import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Bizim Sanal Aşk Kavanozumuz ❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

custom_html = r"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bizim Sanal Aşk Kavanozumuz ❤️</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
        
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #31102f 100%);
            min-height: 100vh;
            color: #f8fafc;
        }

        .font-handwriting {
            font-family: 'Dancing Script', cursive;
        }

        /* Glassmorphism card styles */
        .glass-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.125);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
        }

        /* Jar Container & Heart Animation */
        .jar-glow {
            filter: drop-shadow(0 0 25px rgba(244, 63, 94, 0.35));
        }

        @keyframes floatHeart {
            0% { transform: translateY(0px) rotate(0deg) scale(1); opacity: 0.9; }
            50% { transform: translateY(-15px) rotate(5deg) scale(1.05); opacity: 1; }
            100% { transform: translateY(0px) rotate(0deg) scale(1); opacity: 0.9; }
        }

        .floating-jar {
            animation: floatHeart 4s ease-in-out infinite;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(15, 23, 42, 0.6);
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(244, 63, 94, 0.5);
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(244, 63, 94, 0.8);
        }
    </style>
</head>
<body class="p-4 md:p-8 flex flex-col items-center justify-start min-h-screen">

    <!-- Header Section -->
    <header class="text-center max-w-2xl mx-auto my-6">
        <span class="px-4 py-1.5 rounded-full text-xs font-semibold bg-rose-500/20 text-rose-300 border border-rose-500/30 uppercase tracking-widest inline-block mb-3">
            Sana Özel Hazırlandı 💕
        </span>
        <h1 class="text-4xl md:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-rose-400 via-pink-300 to-purple-400 mb-2">
            Bizim Aşk Kavanozumuz
        </h1>
        <p class="text-slate-300 text-sm md:text-base">
            Senin için kalbimin en derin yerinden gelen küçük sürprizler, anılar ve özel notlar!
        </p>
    </header>

    <!-- Main Navigation Tabs -->
    <div class="flex flex-wrap justify-center gap-2 md:gap-4 mb-8 bg-slate-900/60 p-2 rounded-2xl border border-slate-800">
        <button onclick="switchTab('jar')" id="tab-jar" class="tab-btn px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-300 bg-rose-600 text-white shadow-lg shadow-rose-600/30 flex items-center gap-2">
            <i class="fa-solid font-bold fa-jar-wheat"></i> Aşk Kavanozu
        </button>
        <button onclick="switchTab('envelopes')" id="tab-envelopes" class="tab-btn px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-300 text-slate-400 hover:text-white flex items-center gap-2">
            <i class="fa-solid fa-envelope-open-text"></i> "Beni Ne Zaman Aç?"
        </button>
        <button onclick="switchTab('counter')" id="tab-counter" class="tab-btn px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-300 text-slate-400 hover:text-white flex items-center gap-2">
            <i class="fa-solid fa-clock"></i> Zaman Sayacı
        </button>
    </div>

    <!-- TAB 1: AŞK KAVANOZU -->
    <main id="view-jar" class="w-full max-w-3xl glass-card rounded-3xl p-6 md:p-10 text-center flex flex-col items-center">
        <div class="relative my-4 floating-jar jar-glow cursor-pointer" onclick="drawNote()">
            <!-- SVG Jar Illustration -->
            <svg width="180" height="240" viewBox="0 0 200 260" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Jar Lid -->
                <rect x="50" y="10" width="100" height="20" rx="8" fill="#e2e8f0" stroke="#94a3b8" stroke-width="4"/>
                <rect x="40" y="26" width="120" height="12" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
                <!-- Jar Body -->
                <path d="M45 40 C45 35, 155 35, 155 40 L165 210 C165 240, 35 240, 35 210 Z" fill="rgba(255, 255, 255, 0.08)" stroke="rgba(255, 255, 255, 0.4)" stroke-width="4"/>
                <path d="M50 45 L150 45 L158 205 C158 230, 42 230, 42 205 Z" fill="rgba(244, 63, 94, 0.15)"/>
                <!-- Glowing Hearts Inside -->
                <circle cx="80" cy="140" r="12" fill="#f43f5e" opacity="0.8"/>
                <circle cx="120" cy="160" r="15" fill="#ec4899" opacity="0.8"/>
                <circle cx="100" cy="190" r="10" fill="#fb7185" opacity="0.9"/>
                <circle cx="70" cy="180" r="14" fill="#e11d48" opacity="0.75"/>
                <circle cx="130" cy="120" r="9" fill="#fda4af" opacity="0.9"/>
                <!-- Heart Icon Ribbon -->
                <path d="M100 110 C100 110, 85 90, 70 105 C55 120, 100 150, 100 150 C100 150, 145 120, 130 105 C115 90, 100 110, 100 110 Z" fill="#f43f5e"/>
            </svg>
        </div>

        <p class="text-slate-300 mb-6 text-sm md:text-base max-w-md">
            Kavanoza dokunarak veya aşağıdaki butona basarak sana hazırladığım onlarca özel nottan birini çek! ✨
        </p>

        <button onclick="drawNote()" class="px-8 py-4 bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-600 hover:to-pink-700 text-white font-bold rounded-2xl shadow-lg shadow-rose-500/40 transform hover:scale-105 active:scale-95 transition-all duration-200 flex items-center gap-3">
            <i class="fa-solid fa-heart text-xl"></i> Kavanozdan Not Çek!
        </button>

        <!-- Display Area for Drawn Note -->
        <div id="note-display" class="w-full mt-8 min-h-[140px] flex items-center justify-center p-6 bg-slate-900/70 border border-slate-700/60 rounded-2xl transition-all duration-500">
            <p class="text-slate-400 italic font-medium">
                Kavanoz henüz açılmadı... Bir not çekmek için butona tıkla! 💌
            </p>
        </div>
    </main>

    <!-- TAB 2: "BENİ NE ZAMAN AÇ?" ZARFLARI -->
    <main id="view-envelopes" class="w-full max-w-4xl glass-card rounded-3xl p-6 md:p-10 hidden">
        <h2 class="text-2xl font-bold text-center text-pink-300 mb-2">Özel Durum Mektupları ✉️</h2>
        <p class="text-center text-slate-300 text-sm mb-8">Kendini nasıl hissettiğine göre aşağıdaki mektuplardan birini seç ve oku!</p>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Envelope 1 -->
            <div onclick="openEnvelope(0)" class="bg-slate-800/80 hover:bg-slate-800 border border-rose-500/30 rounded-2xl p-6 text-center cursor-pointer transform hover:-translate-y-1 transition-all duration-300 group shadow-md hover:shadow-rose-500/20">
                <div class="w-14 h-14 bg-rose-500/20 text-rose-400 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-face-sad-tear text-2xl"></i>
                </div>
                <h3 class="font-bold text-slate-100 text-lg mb-1">Moralin Bozuk Olduğunda</h3>
                <p class="text-xs text-slate-400">Gülüşünü hatırlamak istediğin an tıkla.</p>
            </div>

            <!-- Envelope 2 -->
            <div onclick="openEnvelope(1)" class="bg-slate-800/80 hover:bg-slate-800 border border-purple-500/30 rounded-2xl p-6 text-center cursor-pointer transform hover:-translate-y-1 transition-all duration-300 group shadow-md hover:shadow-purple-500/20">
                <div class="w-14 h-14 bg-purple-500/20 text-purple-400 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-moon text-2xl"></i>
                </div>
                <h3 class="font-bold text-slate-100 text-lg mb-1">Gece Uykun Gelmediğinde</h3>
                <p class="text-xs text-slate-400">Aklında ben varken oku.</p>
            </div>

            <!-- Envelope 3 -->
            <div onclick="openEnvelope(2)" class="bg-slate-800/80 hover:bg-slate-800 border border-pink-500/30 rounded-2xl p-6 text-center cursor-pointer transform hover:-translate-y-1 transition-all duration-300 group shadow-md hover:shadow-pink-500/20">
                <div class="w-14 h-14 bg-pink-500/20 text-pink-400 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-heart-crack text-2xl"></i>
                </div>
                <h3 class="font-bold text-slate-100 text-lg mb-1">Beni Çok Özlediğinde</h3>
                <p class="text-xs text-slate-400">Aramızda mesafeler olduğunda tıkla.</p>
            </div>

            <!-- Envelope 4 -->
            <div onclick="openEnvelope(3)" class="bg-slate-800/80 hover:bg-slate-800 border border-amber-500/30 rounded-2xl p-6 text-center cursor-pointer transform hover:-translate-y-1 transition-all duration-300 group shadow-md hover:shadow-amber-500/20">
                <div class="w-14 h-14 bg-amber-500/20 text-amber-400 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-bolt text-2xl"></i>
                </div>
                <h3 class="font-bold text-slate-100 text-lg mb-1">Bana Kızdığında / Kırıldığında</h3>
                <p class="text-xs text-slate-400">Seni ne kadar çok sevdiğimi unutma diye.</p>
            </div>

            <!-- Envelope 5 -->
            <div onclick="openEnvelope(4)" class="bg-slate-800/80 hover:bg-slate-800 border border-emerald-500/30 rounded-2xl p-6 text-center cursor-pointer transform hover:-translate-y-1 transition-all duration-300 group shadow-md hover:shadow-emerald-500/20">
                <div class="w-14 h-14 bg-emerald-500/20 text-emerald-400 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-champagne-glasses text-2xl"></i>
                </div>
                <h3 class="font-bold text-slate-100 text-lg mb-1">Çok Mutlu Olduğunda</h3>
                <p class="text-xs text-slate-400">Sevincini ikiye katlamak için tıkla.</p>
            </div>

            <!-- Envelope 6 -->
            <div onclick="openEnvelope(5)" class="bg-slate-800/80 hover:bg-slate-800 border border-sky-500/30 rounded-2xl p-6 text-center cursor-pointer transform hover:-translate-y-1 transition-all duration-300 group shadow-md hover:shadow-sky-500/20">
                <div class="w-14 h-14 bg-sky-500/20 text-sky-400 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-gift text-2xl"></i>
                </div>
                <h3 class="font-bold text-slate-100 text-lg mb-1">Özel Bir Sürpriz İçin</h3>
                <p class="text-xs text-slate-400">Rastgele bir günde tıkla!</p>
            </div>
        </div>
    </main>

    <!-- TAB 3: ZAMAN SAYACI -->
    <main id="view-counter" class="w-full max-w-2xl glass-card rounded-3xl p-6 md:p-10 text-center hidden">
        <h2 class="text-2xl font-bold text-rose-300 mb-2">Birlikte Geçirdiğimiz Süre ❤️</h2>
        <p class="text-slate-300 text-sm mb-6">İlk tanıştığımız günden itibaren her saniye seni daha çok seviyorum.</p>

        <!-- Timer Display Grid -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 my-6">
            <div class="bg-slate-900/80 p-4 rounded-2xl border border-rose-500/30">
                <span id="cnt-days" class="block text-3xl md:text-4xl font-extrabold text-rose-400">00</span>
                <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider">Gün</span>
            </div>
            <div class="bg-slate-900/80 p-4 rounded-2xl border border-pink-500/30">
                <span id="cnt-hours" class="block text-3xl md:text-4xl font-extrabold text-pink-400">00</span>
                <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider">Saat</span>
            </div>
            <div class="bg-slate-900/80 p-4 rounded-2xl border border-purple-500/30">
                <span id="cnt-minutes" class="block text-3xl md:text-4xl font-extrabold text-purple-400">00</span>
                <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider">Dakika</span>
            </div>
            <div class="bg-slate-900/80 p-4 rounded-2xl border border-indigo-500/30">
                <span id="cnt-seconds" class="block text-3xl md:text-4xl font-extrabold text-indigo-400">00</span>
                <span class="text-xs text-slate-400 font-semibold uppercase tracking-wider">Saniye</span>
            </div>
        </div>

        <p class="text-xs italic text-slate-400 mt-4">
            (Ve bu süre hayatımın en güzel dönemi...)
        </p>
    </main>

    <!-- Modal for Letters -->
    <div id="letter-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-slate-900 border border-rose-500/40 w-full max-w-lg rounded-3xl p-6 md:p-8 relative shadow-2xl animate-fade-in">
            <button onclick="closeModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center">
                <i class="fa-solid fa-xmark"></i>
            </button>
            <h3 id="modal-title" class="text-xl font-bold text-rose-400 mb-4 pr-6"></h3>
            <div id="modal-body" class="text-slate-200 text-sm md:text-base leading-relaxed space-y-3 font-handwriting text-2xl"></div>
            <div class="mt-6 text-right">
                <button onclick="closeModal()" class="px-5 py-2 bg-rose-600 hover:bg-rose-700 text-white font-semibold rounded-xl text-sm">
                    Kapat 💖
                </button>
            </div>
        </div>
    </div>

    <!-- Scripting Logic -->
    <script>
        // --- 1. AŞK KAVANOZU NOTLARI ---
        const jarNotes = [
            "Gülüşün benim için dünyadaki en huzurlu manzara. 😊",
            "Seninle içilen tek bir bardak çayın bile tadı bambaşka. ☕",
            "Gözlerinin içine baktığımda zamanın durmasını istiyorum. ✨",
            "Bana hissettirdiğin o kocaman güven hissi için teşekkür ederim. 🛡️",
            "En saçma şakalarıma bile benimle birlikte gülmeni seviyorum! 😂",
            "Sen benim bu hayattaki en doğru kararımsın. ❤️",
            "Kötü bir günün ardından sadece sesini duymak bile tüm yorgunluğumu alıyor. 🎧",
            "Seninle geçirdiğim her saniye benim için paha biçilemez bir anı. ⏳",
            "Birlikte saçmalayabilmemiz, bir çocuk gibi eğlenebilmemiz paha biçilemez! 🎈",
            "Sadece bugün değil, her gün seni daha çok seviyorum. 🔥",
            "Ellerini tuttuğum an tüm dünya dışarıda kalıyor. 🤝",
            "Sen benim hem en yakın arkadaşım hem de kalbimin sahibisin. 👑",
            "Yüzündeki o tatlı tebessüm hiç ama hiç eksik olmasın. 🌟",
            "Seninle yaşlanmak, hayatın bana sunduğu en güzel hediye olurdu. 👵👴",
            "İyi ki varsın, iyi ki benimlesin sevgilim! 💖"
        ];

        function drawNote() {
            const randomIndex = Math.floor(Math.random() * jarNotes.length);
            const noteDisplay = document.getElementById('note-display');
            
            // Confetti Effect
            confetti({
                particleCount: 40,
                spread: 60,
                origin: { y: 0.7 }
            });

            noteDisplay.style.opacity = 0;
            setTimeout(() => {
                noteDisplay.innerHTML = `
                    <div class="animate-bounce mb-2 text-rose-400 text-2xl">💌</div>
                    <p class="text-rose-200 text-lg md:text-xl font-medium font-handwriting tracking-wide">
                        "${jarNotes[randomIndex]}"
                    </p>
                `;
                noteDisplay.style.opacity = 1;
            }, 200);
        }

        // --- 2. ZARF MEKTUPLARI ---
        const envelopesData = [
            {
                title: "Moralin Bozuk Olduğunda 🥺",
                content: "Biliyorum bazen her şey üst üste gelebilir. Ama lütfen unutma, senin o güzel gülüşün her zorluğu yenecek kadar güçlü. Ben her zaman buradayım, elini tutmak ve seni güldürmek için bekliyorum. Derin bir nefes al ve ne kadar özel olduğunu hatırla!"
            },
            {
                title: "Gece Uykun Gelmediğinde 🌙",
                content: "Gecenin bu saatinde aklına düştüysem, bil ki şu an benim de dualarımda ve kalbimdesin. Gözlerini kapat, başını yastığa koy ve rüyanda birlikte yürüdüğümüz o huzurlu yolları düşün. İyi uykular sevgilim, sabaha yine seninle uyanmak dileğiyle..."
            },
            {
                title: "Beni Çok Özlediğinde 🫂",
                content: "Aramızda ne kadar mesafe olursa olsun, kalbimin ritmi hep senin yanında atıyor. Şu an sana sarılamıyor olabilirim ama bil ki en kısa sürede kavuşacağız. Şimdi gözlerini kapat ve sana sımsıkı sarıldığımı hisset!"
            },
            {
                title: "Bana Kızdığında veya Kırıldığında 💔",
                content: "Eğer seni üzecek bir şey yaptıysam kalpten özür dilerim. Seni kırmak isteyeceğim en son şey bile olamaz. Lütfen kalbini bana kapatma, gel konuşalım ve sarılarak çözelim. Sen benim her şeyimsin."
            },
            {
                title: "Çok Mutlu Olduğunda 🎉",
                content: "Senin mutluluğun benim en büyük neşem! Yüzündeki o ışığı görebiliyorum ve seninle gurur duyuyorum. Mutluluğumuzu kutlamak için sabırsızlanıyorum, sen her zaman en güzellerine layıksın!"
            },
            {
                title: "Sürpriz Bir Mektup 🎁",
                content: "Sadece rastgele bir günde karşına çıkmak istedim! Hiçbir sebep yokken bile seni düşündüğümü, seni her gün daha da tutkuyla sevdiğimi bilmeni istedim. İyi ki hayatımdasın güzel insan!"
            }
        ];

        function openEnvelope(index) {
            const data = envelopesData[index];
            document.getElementById('modal-title').innerText = data.title;
            document.getElementById('modal-body').innerText = data.content;
            document.getElementById('letter-modal').classList.remove('hidden');

            confetti({
                particleCount: 50,
                spread: 70,
                origin: { y: 0.5 }
            });
        }

        function closeModal() {
            document.getElementById('letter-modal').classList.add('hidden');
        }

        // --- 3. TAB DEĞİŞTİRME LOGİC ---
        function switchTab(tabName) {
            document.getElementById('view-jar').classList.add('hidden');
            document.getElementById('view-envelopes').classList.add('hidden');
            document.getElementById('view-counter').classList.add('hidden');

            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.className = 'tab-btn px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-300 text-slate-400 hover:text-white flex items-center gap-2';
            });

            if(tabName === 'jar') {
                document.getElementById('view-jar').classList.remove('hidden');
                document.getElementById('tab-jar').className = 'tab-btn px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-300 bg-rose-600 text-white shadow-lg shadow-rose-600/30 flex items-center gap-2';
            } else if(tabName === 'envelopes') {
                document.getElementById('view-envelopes').classList.remove('hidden');
                document.getElementById('tab-envelopes').className = 'tab-btn px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-300 bg-rose-600 text-white shadow-lg shadow-rose-600/30 flex items-center gap-2';
            } else if(tabName === 'counter') {
                document.getElementById('view-counter').classList.remove('hidden');
                document.getElementById('tab-counter').className = 'tab-btn px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-300 bg-rose-600 text-white shadow-lg shadow-rose-600/30 flex items-center gap-2';
            }
        }

        // --- 4. CANLI ZAMAN SAYACI ---
        // Başlangıç tarihini buradan özelleştirebilirsiniz (Örn: 1 Ocak 2023)
        const startDate = new Date("2023-01-01T00:00:00");

        function updateCounter() {
            const now = new Date();
            const diff = now - startDate;

            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
            const minutes = Math.floor((diff / 1000 / 60) % 60);
            const seconds = Math.floor((diff / 1000) % 60);

            document.getElementById('cnt-days').innerText = days < 10 ? '0' + days : days;
            document.getElementById('cnt-hours').innerText = hours < 10 ? '0' + hours : hours;
            document.getElementById('cnt-minutes').innerText = minutes < 10 ? '0' + minutes : minutes;
            document.getElementById('cnt-seconds').innerText = seconds < 10 ? '0' + seconds : seconds;
        }

        setInterval(updateCounter, 1000);
        updateCounter();
    </script>
</body>
</html>
"""

html(custom_html, height=850, scrolling=True)