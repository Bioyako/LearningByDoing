// --- State management ---
let currentTheme = "dark";
let sidebarClosed = false;

// Funzione immediata (poiché lo script è alla fine del body)
(function init() {
  // 1. Applica tema di default
  setDark();
  
  // 2. Setup theme button
  const tbtn = document.getElementById("theme-toggle");
  if (tbtn) {
    tbtn.onclick = toggleTheme; // Usa onclick diretto per sicurezza
  }

  // 3. Setup sidebar button
  const sbtn = document.getElementById("sidebar-toggle");
  if (sbtn) {
    sbtn.onclick = toggleSidebar;
  }
})();

// --- Theme functions ---
function toggleTheme() {
  if (currentTheme === "light") { 
    setDark(); 
  } else { 
    setLight(); 
  }
}

function setDark() {
  document.documentElement.classList.add("dark-mode");
  document.documentElement.classList.remove("light-mode");
  currentTheme = "dark";
  
  const btn = document.getElementById("theme-toggle");
  if (btn) { 
    btn.textContent = "🌙 Dark Mode";
    btn.style.background = "#232b3a"; 
    btn.style.color = "#d4d4d4"; 
  }
}

function setLight() {
  document.documentElement.classList.add("light-mode");
  document.documentElement.classList.remove("dark-mode");
  currentTheme = "light";
  
  const btn = document.getElementById("theme-toggle");
  if (btn) { 
    btn.textContent = "☀️ Light Mode";
    btn.style.background = "#e8e8e8"; 
    btn.style.color = "#1e2433"; 
  }
}

// --- Sidebar functions ---
function toggleSidebar() {
  // Toggle class on root (HTML) element
  sidebarClosed = !sidebarClosed;
  if (sidebarClosed) {
    document.documentElement.classList.add("sidebar-closed");
  } else {
    document.documentElement.classList.remove("sidebar-closed");
  }
}
