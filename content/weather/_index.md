---
title: "Weather"
layout: "list"
summary: "On-demand Nice Weather Index (NWI) comfort checker."
hideMeta: true
ShowToc: false
build:
  list: "never"
  render: "always"
sitemap:
  disable: true
---
<div id="nwi-widget-root" class="nwi-widget-container">
<div class="nwi-glass-card">
<div class="nwi-header">
<div class="nwi-title-area">
<h1>Nice Weather Index</h1>
<p class="nwi-subtitle">On-Demand Comfort Index & Action Plan</p>
</div>
<div class="nwi-location-info">
<span id="nwi-city-name">Grand Meadow, MN</span>
<span id="nwi-coords">43.71°N, -92.28°W</span>
</div>
</div>
<!-- Location Selector Tabs -->
<div class="nwi-tabs">
<button class="nwi-tab-btn active" onclick="setNwiLocation('home', 43.71, -92.28, 'Grand Meadow, MN (Home)')">🏡 Home</button>
<button class="nwi-tab-btn" onclick="setNwiLocation('office', 43.86, -92.19, 'Stewartville, MN (Office)')">🏢 Office</button>
<button class="nwi-tab-btn" onclick="detectNwiLocation()">📍 Current GPS</button>
<div class="nwi-search-wrapper">
<input type="text" id="nwi-search-input" placeholder="Search world cities..." oninput="searchNwiCities()">
<div id="nwi-search-results" class="nwi-search-results-dropdown"></div>
</div>
</div>
<!-- Main Score Display -->
<div class="nwi-main-dashboard">
<div id="nwi-hero-gradient" class="nwi-hero-card">
<div class="nwi-gauge-wrapper">
<svg class="nwi-gauge" viewBox="0 0 120 120">
<circle class="nwi-gauge-bg" cx="60" cy="60" r="54"></circle>
<circle id="nwi-gauge-fill" class="nwi-gauge-fill" cx="60" cy="60" r="54" stroke-dasharray="339.29" stroke-dashoffset="339.29"></circle>
</svg>
<div class="nwi-gauge-text">
<span id="nwi-score-num">0.0</span>
<span class="nwi-score-scale">/10</span>
</div>
</div>
<div class="nwi-hero-meta">
<h2 id="nwi-classification-text">Calculating...</h2>
<p id="nwi-summary-stats">Loading current conditions...</p>
</div>
</div>
</div>
<!-- Action Plan Card -->
<div class="nwi-section-title">⚡ Today's Action Plan</div>
<div class="nwi-action-plan-grid">
<div class="nwi-action-card">
<div id="nwi-advice-windows" class="nwi-action-content">
Loading window open/closed advice...
</div>
</div>
<div class="nwi-action-card">
<div id="nwi-advice-outdoors" class="nwi-action-content">
Loading outdoor activity recommendations...
</div>
</div>
</div>
<!-- 24-Hour Timeline Section -->
<div class="nwi-section-title">📈 24-Hour Comfort Timeline</div>
<div class="nwi-timeline-card">
<div id="nwi-timeline-tooltip" class="nwi-timeline-tooltip"></div>
<div class="nwi-timeline-scroll-container">
<div id="nwi-hourly-timeline" class="nwi-hourly-timeline">
<div class="nwi-timeline-loading">Loading 24-hour comfort timeline...</div>
</div>
</div>
<div class="nwi-timeline-legend">
  <div class="nwi-indicator-legend">
    <div class="nwi-legend-item">
      <span class="nwi-indicator-dot active-window" style="display:inline-block; width: 8px; height: 8px; border-radius: 50%;"></span>
      Open Windows
    </div>
    <div class="nwi-legend-item">
      <span class="nwi-indicator-dot active-outdoor" style="display:inline-block; width: 8px; height: 8px; border-radius: 50%;"></span>
      Outdoors
    </div>
  </div>
</div>
</div>
<!-- Hourly Snapshots -->
<div class="nwi-section-title">🕒 Comfort Snapshots</div>
<div class="nwi-snapshots-grid">
<div class="nwi-snapshot-card">
<div class="nwi-snap-time">8:00 AM</div>
<div id="nwi-snap-score-8a" class="nwi-snap-score">-.--</div>
<div id="nwi-snap-details-8a" class="nwi-snap-details">--°F | Dew: --°F<br>-- mph | --</div>
</div>
<div class="nwi-snapshot-card">
<div class="nwi-snap-time">12:00 PM</div>
<div id="nwi-snap-score-12p" class="nwi-snap-score">-.--</div>
<div id="nwi-snap-details-12p" class="nwi-snap-details">--°F | Dew: --°F<br>-- mph | --</div>
</div>
<div class="nwi-snapshot-card">
<div class="nwi-snap-time">4:00 PM</div>
<div id="nwi-snap-score-4p" class="nwi-snap-score">-.--</div>
<div id="nwi-snap-details-4p" class="nwi-snap-details">--°F | Dew: --°F<br>-- mph | --</div>
</div>
<div class="nwi-snapshot-card">
<div class="nwi-snap-time">8:00 PM</div>
<div id="nwi-snap-score-8p" class="nwi-snap-score">-.--</div>
<div id="nwi-snap-details-8p" class="nwi-snap-details">--°F | Dew: --°F<br>-- mph | --</div>
</div>
</div>
</div>
</div>
<style>
/* NWI Widget Styling - Scoped to root container */
.nwi-widget-container {
margin: 2rem 0;
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
color: #1d1d1f;
}
/* Glassmorphism card container */
.nwi-glass-card {
background: rgba(255, 255, 255, 0.7);
backdrop-filter: blur(20px);
-webkit-backdrop-filter: blur(20px);
border: 1px solid rgba(0, 0, 0, 0.06);
border-radius: 24px;
padding: 2.5rem;
box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03);
transition: all 0.3s ease;
}
/* Dark mode overrides */
.dark .nwi-glass-card {
background: rgba(24, 24, 26, 0.7);
border: 1px solid rgba(255, 255, 255, 0.08);
box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
color: #f5f5f7;
}
/* Header layout */
.nwi-header {
display: flex;
justify-content: space-between;
align-items: flex-start;
flex-wrap: wrap;
gap: 1.5rem;
margin-bottom: 2rem;
border-bottom: 1px solid rgba(0, 0, 0, 0.05);
padding-bottom: 1.5rem;
}
.dark .nwi-header {
border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}
.nwi-title-area h1 {
font-size: 2.2rem;
font-weight: 800;
margin: 0;
letter-spacing: -0.03em;
line-height: 1.1;
display: flex;
align-items: center;
gap: 0.75rem;
}
.nwi-subtitle {
font-size: 1rem;
color: #86868b;
margin: 0.4rem 0 0 0;
}
.nwi-location-info {
display: flex;
flex-direction: column;
align-items: flex-end;
text-align: right;
}
#nwi-city-name {
font-size: 1.25rem;
font-weight: 700;
letter-spacing: -0.01em;
}
#nwi-coords {
font-size: 0.85rem;
color: #86868b;
margin-top: 0.2rem;
}
/* Tabs & Search controls */
.nwi-tabs {
display: flex;
align-items: center;
gap: 0.75rem;
margin-bottom: 2rem;
flex-wrap: wrap;
}
.nwi-tab-btn {
background: rgba(0, 0, 0, 0.03);
border: 1px solid rgba(0, 0, 0, 0.05);
border-radius: 14px;
padding: 0.6rem 1.2rem;
font-size: 0.9rem;
font-weight: 600;
cursor: pointer;
transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
color: inherit;
}
.dark .nwi-tab-btn {
background: rgba(255, 255, 255, 0.03);
border: 1px solid rgba(255, 255, 255, 0.05);
}
.nwi-tab-btn:hover {
background: rgba(0, 0, 0, 0.08);
transform: translateY(-1px);
}
.dark .nwi-tab-btn:hover {
background: rgba(255, 255, 255, 0.08);
}
.nwi-tab-btn.active {
background: #1d1d1f;
color: #fff;
border-color: #1d1d1f;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
.dark .nwi-tab-btn.active {
background: #f5f5f7;
color: #1d1d1f;
border-color: #f5f5f7;
box-shadow: 0 4px 12px rgba(255, 255, 255, 0.1);
}
/* World Search Auto-complete Input */
.nwi-search-wrapper {
position: relative;
flex-grow: 1;
min-width: 200px;
}
#nwi-search-input {
width: 100%;
background: rgba(0, 0, 0, 0.03);
border: 1px solid rgba(0, 0, 0, 0.05);
border-radius: 14px;
padding: 0.6rem 1.2rem;
font-size: 0.9rem;
font-weight: 500;
outline: none;
transition: all 0.2s ease;
color: inherit;
}
.dark #nwi-search-input {
background: rgba(255, 255, 255, 0.03);
border: 1px solid rgba(255, 255, 255, 0.05);
}
#nwi-search-input:focus {
background: rgba(255, 255, 255, 1);
border-color: #0071e3;
box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.15);
}
.dark #nwi-search-input:focus {
background: rgba(30, 30, 30, 1);
border-color: #0071e3;
box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.3);
}
.nwi-search-results-dropdown {
position: absolute;
top: calc(100% + 6px);
left: 0;
right: 0;
background: rgba(255, 255, 255, 0.95);
backdrop-filter: blur(20px);
-webkit-backdrop-filter: blur(20px);
border: 1px solid rgba(0, 0, 0, 0.1);
border-radius: 14px;
box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
z-index: 100;
max-height: 240px;
overflow-y: auto;
display: none;
}
.dark .nwi-search-results-dropdown {
background: rgba(30, 30, 30, 0.95);
border: 1px solid rgba(255, 255, 255, 0.1);
}
.nwi-search-item {
padding: 0.75rem 1.2rem;
cursor: pointer;
font-size: 0.85rem;
font-weight: 500;
transition: background 0.15s ease;
border-bottom: 1px solid rgba(0, 0, 0, 0.03);
}
.dark .nwi-search-item {
border-bottom: 1px solid rgba(255, 255, 255, 0.03);
}
.nwi-search-item:hover {
background: rgba(0, 113, 227, 0.08);
}
/* Hero card displaying the calculated score and weather metadata */
.nwi-main-dashboard {
margin-bottom: 2.5rem;
}
.nwi-hero-card {
padding: 2.5rem;
border-radius: 20px;
display: flex;
align-items: center;
gap: 2.5rem;
transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
background: #ffffff;
border: 1px solid rgba(0, 0, 0, 0.08);
box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
}
.dark .nwi-hero-card {
background: rgba(255, 255, 255, 0.02);
border: 1px solid rgba(255, 255, 255, 0.08);
box-shadow: none;
}
/* NWI Score Circular SVG Gauge */
.nwi-gauge-wrapper {
position: relative;
width: 130px;
height: 130px;
flex-shrink: 0;
}
.nwi-gauge {
width: 100%;
height: 100%;
transform: rotate(-90deg);
}
.nwi-gauge-bg {
fill: none;
stroke: rgba(0, 0, 0, 0.06);
stroke-width: 8;
}
.dark .nwi-gauge-bg {
stroke: rgba(255, 255, 255, 0.08);
}
.nwi-gauge-fill {
fill: none;
stroke: url(#nwi-grad-glorious);
stroke-width: 8;
stroke-linecap: round;
transition: stroke-dashoffset 1s cubic-bezier(0.16, 1, 0.3, 1);
}
.nwi-gauge-text {
position: absolute;
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
}
#nwi-score-num {
font-size: 2.4rem;
font-weight: 800;
letter-spacing: -0.04em;
line-height: 1;
}
.nwi-score-scale {
font-size: 0.8rem;
color: #86868b;
font-weight: 700;
}
.nwi-hero-meta {
flex-grow: 1;
}
.nwi-hero-meta h2 {
font-size: 2rem;
font-weight: 800;
margin: 0 0 0.5rem 0;
letter-spacing: -0.03em;
background: linear-gradient(135deg, #1d1d1f, #86868b);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}
.dark .nwi-hero-meta h2 {
background: linear-gradient(135deg, #ffffff, #86868b);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}
#nwi-summary-stats {
font-size: 1.05rem;
color: #515154;
margin: 0;
line-height: 1.45;
font-weight: 500;
}
.dark #nwi-summary-stats {
color: #d2d2d7;
}
/* Sections titles */
.nwi-section-title {
font-size: 1.2rem;
font-weight: 750;
letter-spacing: -0.01em;
margin-bottom: 1.2rem;
text-transform: uppercase;
color: #86868b;
font-size: 0.85rem;
letter-spacing: 0.08em;
}
/* Action Plan layouts */
.nwi-action-plan-grid {
display: grid;
grid-template-columns: 1fr 1fr;
gap: 1.2rem;
margin-bottom: 2.5rem;
}
@media (max-width: 768px) {
.nwi-action-plan-grid {
grid-template-columns: 1fr;
}
}
.nwi-action-card {
background: #ffffff;
border: 1px solid rgba(0, 0, 0, 0.08);
border-radius: 18px;
padding: 1.5rem;
transition: transform 0.2s ease, box-shadow 0.2s ease;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
}
.dark .nwi-action-card {
background: rgba(255, 255, 255, 0.02);
border: 1px solid rgba(255, 255, 255, 0.08);
box-shadow: none;
}
.nwi-action-card:hover {
transform: translateY(-2px);
box-shadow: 0 6px 20px rgba(0, 0, 0, 0.04);
}
.nwi-action-content {
font-size: 0.95rem;
line-height: 1.5;
font-weight: 500;
}
/* Timeline Layout & Styling */
.nwi-timeline-card {
position: relative;
background: #ffffff;
border: 1px solid rgba(0, 0, 0, 0.08);
border-radius: 20px;
padding: 1.5rem;
margin-bottom: 2.5rem;
box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
}
.dark .nwi-timeline-card {
position: relative;
background: rgba(255, 255, 255, 0.02);
border: 1px solid rgba(255, 255, 255, 0.08);
box-shadow: none;
}
.nwi-timeline-scroll-container {
width: 100%;
overflow-x: auto;
padding: 1rem 0;
-webkit-overflow-scrolling: touch;
scrollbar-width: thin;
}
/* Custom Scrollbar */
.nwi-timeline-scroll-container::-webkit-scrollbar {
height: 6px;
}
.nwi-timeline-scroll-container::-webkit-scrollbar-track {
background: rgba(0, 0, 0, 0.02);
border-radius: 3px;
}
.dark .nwi-timeline-scroll-container::-webkit-scrollbar-track {
background: rgba(255, 255, 255, 0.02);
}
.nwi-timeline-scroll-container::-webkit-scrollbar-thumb {
background: rgba(0, 0, 0, 0.1);
border-radius: 3px;
}
.dark .nwi-timeline-scroll-container::-webkit-scrollbar-thumb {
background: rgba(255, 255, 255, 0.15);
}
.nwi-hourly-timeline {
display: flex;
justify-content: space-between;
gap: 0.4rem;
min-width: 680px;
height: 190px;
align-items: flex-end;
}
.nwi-timeline-column {
display: flex;
flex-direction: column;
align-items: center;
flex: 1;
height: 100%;
justify-content: flex-end;
position: relative;
}
.nwi-timeline-score-label {
font-size: 0.75rem;
font-weight: 700;
margin-bottom: 0.4rem;
opacity: 0.85;
}
.nwi-timeline-bar-wrapper {
width: 100%;
height: 110px;
display: flex;
align-items: flex-end;
justify-content: center;
}
.nwi-timeline-bar {
width: 14px;
border-radius: 4px 4px 0 0;
transition: height 1.2s cubic-bezier(0.16, 1, 0.3, 1), transform 0.2s ease, box-shadow 0.2s ease;
cursor: pointer;
}
.nwi-timeline-bar:hover {
transform: scaleY(1.05);
box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}
.nwi-timeline-column.current-hour .nwi-timeline-bar {
outline: 2px solid #0071e3;
outline-offset: 2px;
}
.dark .nwi-timeline-column.current-hour .nwi-timeline-bar {
outline: 2px solid #0055ff;
}
.nwi-timeline-indicators {
display: flex;
gap: 3px;
justify-content: center;
margin-top: 0.3rem;
height: 6px;
}
.nwi-indicator-dot {
width: 5px;
height: 5px;
border-radius: 50%;
background: transparent;
transition: all 0.2s ease;
}
.nwi-indicator-dot.active-window {
background: #10b981;
}
.nwi-indicator-dot.active-outdoor {
background: #0071e3;
}
.nwi-timeline-hour-label {
font-size: 0.75rem;
font-weight: 600;
color: #86868b;
margin-top: 0.5rem;
text-transform: uppercase;
white-space: nowrap;
}
.nwi-timeline-column.current-hour .nwi-timeline-hour-label {
color: #0071e3;
font-weight: 800;
}
.dark .nwi-timeline-column.current-hour .nwi-timeline-hour-label {
color: #0055ff;
}
.nwi-timeline-legend {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.2rem;
  margin-top: 1.5rem;
  border-top: 1px solid rgba(0, 0, 0, 0.08);
  padding-top: 1.2rem;
}
.dark .nwi-timeline-legend {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
.nwi-indicator-legend {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  width: 100%;
}
.nwi-legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  font-weight: 700;
  color: #515154;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.dark .nwi-legend-item {
  color: #d2d2d7;
}
/* Tooltip styling */
.nwi-timeline-tooltip {
position: absolute;
background: rgba(29, 29, 31, 0.95);
color: #fff;
padding: 0.6rem 0.8rem;
border-radius: 10px;
font-size: 0.75rem;
white-space: nowrap;
z-index: 1000;
opacity: 0;
visibility: hidden;
transition: opacity 0.15s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.15s cubic-bezier(0.16, 1, 0.3, 1), transform 0.15s cubic-bezier(0.16, 1, 0.3, 1);
transform: translate(-50%, -100%) translateY(10px);
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
pointer-events: none;
text-align: left;
line-height: 1.4;
border: 1px solid rgba(255, 255, 255, 0.1);
}
.dark .nwi-timeline-tooltip {
background: rgba(255, 255, 255, 0.95);
color: #1d1d1f;
border: 1px solid rgba(0, 0, 0, 0.1);
}
.nwi-timeline-tooltip.visible {
opacity: 1;
visibility: visible;
transform: translate(-50%, -100%) translateY(0);
}
/* Timeline Bar Color Classes */
.bg-glorious { background: linear-gradient(to top, #f97316, #facc15); }
.bg-great { background: linear-gradient(to top, #2563eb, #60a5fa); }
.bg-pleasant { background: linear-gradient(to top, #059669, #34d399); }
.bg-mediocre { background: linear-gradient(to top, #4f46e5, #818cf8); }
.bg-unpleasant { background: linear-gradient(to top, #475569, #94a3b8); }
/* Snapshots Layout */
.nwi-snapshots-grid {
display: grid !important;
grid-template-columns: repeat(4, 1fr) !important;
gap: 1.2rem !important;
width: 100% !important;
box-sizing: border-box;
}
@media (max-width: 768px) {
.nwi-snapshots-grid {
grid-template-columns: repeat(2, 1fr) !important;
}
}
@media (max-width: 480px) {
.nwi-snapshots-grid {
grid-template-columns: 1fr !important;
}
}
.nwi-snapshot-card {
background: #ffffff;
border: 1px solid rgba(0, 0, 0, 0.08);
border-radius: 18px;
padding: 1.5rem 1.2rem;
text-align: center;
transition: all 0.2s ease;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
}
.dark .nwi-snapshot-card {
background: rgba(255, 255, 255, 0.02);
border: 1px solid rgba(255, 255, 255, 0.08);
box-shadow: none;
}
.nwi-snapshot-card:hover {
transform: translateY(-3px);
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
}
.nwi-snap-time {
font-size: 0.85rem;
font-weight: 700;
color: #86868b;
text-transform: uppercase;
margin-bottom: 0.6rem;
}
.nwi-snap-score {
font-size: 1.8rem;
font-weight: 800;
letter-spacing: -0.03em;
margin-bottom: 0.6rem;
}
.nwi-snap-details {
font-size: 0.8rem;
line-height: 1.4;
color: #515154;
font-weight: 500;
}
.dark .nwi-snap-details {
color: #d2d2d7;
}
/* Dynamic color definitions */
.color-glorious { color: #f97316; }
.color-great { color: #3b82f6; }
.color-pleasant { color: #10b981; }
.color-mediocre { color: #6366f1; }
.color-unpleasant { color: #64748b; }
.dark .color-glorious { color: #fb923c; }
.dark .color-great { color: #60a5fa; }
.dark .color-pleasant { color: #34d399; }
.dark .color-mediocre { color: #818cf8; }
.dark .color-unpleasant { color: #94a3b8; }
</style>
<!-- SVG Gradients for circular gauge -->
<svg style="width:0; height:0; position:absolute;" aria-hidden="true" focusable="false">
<defs>
<linearGradient id="nwi-grad-glorious" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#facc15" />
<stop offset="100%" stop-color="#f97316" />
</linearGradient>
<linearGradient id="nwi-grad-great" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#60a5fa" />
<stop offset="100%" stop-color="#2563eb" />
</linearGradient>
<linearGradient id="nwi-grad-pleasant" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#34d399" />
<stop offset="100%" stop-color="#059669" />
</linearGradient>
<linearGradient id="nwi-grad-mediocre" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#818cf8" />
<stop offset="100%" stop-color="#4f46e5" />
</linearGradient>
<linearGradient id="nwi-grad-unpleasant" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#94a3b8" />
<stop offset="100%" stop-color="#475569" />
</linearGradient>
</defs>
</svg>
<script>
// NWI Calculation and UI Engine
const nwiLocations = {
home: { lat: 43.71, lon: -92.28, name: "Grand Meadow, MN (Home)" },
office: { lat: 43.86, lon: -92.19, name: "Stewartville, MN (Office)" }
};
let currentNwiLocation = nwiLocations.home;
// Execute calculations on page load
document.addEventListener("DOMContentLoaded", () => {
fetchNwiWeather(currentNwiLocation.lat, currentNwiLocation.lon, currentNwiLocation.name);
// Close search suggestion dropdown on outer click
document.addEventListener("click", (e) => {
if (!e.target.closest(".nwi-search-wrapper")) {
document.getElementById("nwi-search-results").style.display = "none";
}
});
});
function calculateNwiScore(temp, dewPoint, precipProb, windSpeed, weatherCode) {
// 1. Temperature Score (30%) - Continuous Bounds
let tempScore = 0;
if (temp >= 64 && temp <= 72) tempScore = 10;
else if ((temp >= 60 && temp < 64) || (temp > 72 && temp <= 76)) tempScore = 9;
else if ((temp >= 55 && temp < 60) || (temp > 76 && temp <= 80)) tempScore = 7;
else if ((temp >= 50 && temp < 55) || (temp > 80 && temp <= 85)) tempScore = 5;
else if ((temp >= 40 && temp < 50) || (temp > 85 && temp <= 90)) tempScore = 3;
else tempScore = 0;
// 2. Humidity/Dew Point Score (25%) - Continuous Bounds
let dewScore = 0;
if (dewPoint <= 52) dewScore = 10;
else if (dewPoint > 52 && dewPoint <= 56) dewScore = 9;
else if (dewPoint > 56 && dewPoint <= 60) dewScore = 7;
else if (dewPoint > 60 && dewPoint <= 64) dewScore = 4;
else if (dewPoint > 64 && dewPoint <= 68) dewScore = 1;
else dewScore = 0;
// Cold dry air override - aligned with cooler zone
if (temp < 60) {
dewScore = 10;
}
// 3. Precipitation Score (25%) - Continuous Bounds
let precipScore = 0;
if (precipProb >= 0 && precipProb <= 5) precipScore = 10;
else if (precipProb > 5 && precipProb <= 15) precipScore = 9;
else if (precipProb > 15 && precipProb <= 30) precipScore = 7;
else if (precipProb > 30 && precipProb <= 50) precipScore = 4;
else if (precipProb > 50 && precipProb <= 70) precipScore = 2;
else precipScore = 0;
// 4. Wind Score (10%) - Continuous Bounds
let windScore = 0;
if (windSpeed <= 5) windScore = 10;
else if (windSpeed > 5 && windSpeed <= 11) windScore = 9;
else if (windSpeed > 11 && windSpeed <= 15) windScore = 6;
else if (windSpeed > 15 && windSpeed <= 20) windScore = 3;
else windScore = 0;
// 5. Sky Conditions Score (10%) - Kept well-calibrated
let skyScore = 7;
if (weatherCode === 0 || weatherCode === 1) skyScore = 10;
else if (weatherCode === 2) skyScore = 9;
else if (weatherCode === 3) skyScore = 7;
else if (weatherCode === 45 || weatherCode === 48) skyScore = 5;
else if (weatherCode >= 51 && weatherCode <= 55) skyScore = 4;
else if ((weatherCode >= 61 && weatherCode <= 65) || (weatherCode >= 80 && weatherCode <= 82)) skyScore = 2;
else if ((weatherCode >= 71 && weatherCode <= 77) || (weatherCode >= 85 && weatherCode <= 86)) skyScore = 1;
else if (weatherCode >= 95 && weatherCode <= 99) skyScore = 0;
const nwi = (tempScore * 0.3) + (dewScore * 0.25) + (precipScore * 0.25) + (windScore * 0.1) + (skyScore * 0.1);
return Math.round(nwi * 10) / 10;
}
function getNwiClassification(score) {
if (score >= 9.0) return { text: "Glorious", class: "color-glorious", grad: "nwi-grad-glorious" };
if (score >= 7.5) return { text: "Great", class: "color-great", grad: "nwi-grad-great" };
if (score >= 6.0) return { text: "Pleasant", class: "color-pleasant", grad: "nwi-grad-pleasant" };
if (score >= 4.5) return { text: "Mediocre", class: "color-mediocre", grad: "nwi-grad-mediocre" };
return { text: "Unpleasant", class: "color-unpleasant", grad: "nwi-grad-unpleasant" };
}
function getWeatherWmoText(code) {
if (code === 0) return "Clear sky";
if (code === 1) return "Mainly clear";
if (code === 2) return "Partly cloudy";
if (code === 3) return "Overcast";
if (code === 45 || code === 48) return "Foggy";
if (code >= 51 && code <= 55) return "Drizzle";
if (code >= 61 && code <= 65) return "Rain";
if (code >= 71 && code <= 77) return "Snow";
if (code >= 80 && code <= 82) return "Rain showers";
if (code >= 85 && code <= 86) return "Snow showers";
if (code >= 95 && code <= 99) return "Thunderstorm";
return "Overcast";
}
function formatHourAmPm(h) {
if (h === 0) return "12:00 AM";
if (h === 12) return "12:00 PM";
if (h > 12) return `${h - 12}:00 PM`;
return `${h}:00 AM`;
}
function setNwiLocation(tabId, lat, lon, name) {
// Update active tab styles
document.querySelectorAll(".nwi-tab-btn").forEach(btn => btn.classList.remove("active"));
if (tabId === "home") {
document.querySelectorAll(".nwi-tab-btn")[0].classList.add("active");
} else if (tabId === "office") {
document.querySelectorAll(".nwi-tab-btn")[1].classList.add("active");
}
currentNwiLocation = { lat, lon, name };
fetchNwiWeather(lat, lon, name);
}
function detectNwiLocation() {
const gpsBtn = document.querySelectorAll(".nwi-tab-btn")[2];
gpsBtn.innerText = "📍 Locating...";
if (!navigator.geolocation) {
gpsBtn.innerText = "📍 GPS Failed";
alert("Geolocation is not supported by your browser.");
return;
}
navigator.geolocation.getCurrentPosition(
(position) => {
document.querySelectorAll(".nwi-tab-btn").forEach(btn => btn.classList.remove("active"));
gpsBtn.classList.add("active");
gpsBtn.innerText = "📍 GPS Active";
const lat = Math.round(position.coords.latitude * 100) / 100;
const lon = Math.round(position.coords.longitude * 100) / 100;
const name = `Detected Location (${lat}°N, ${lon}°W)`;
fetchNwiWeather(lat, lon, name);
},
(err) => {
gpsBtn.innerText = "📍 GPS Blocked";
console.warn(`Geolocation error (${err.code}): ${err.message}`);
alert("Unable to fetch location. Please search manually or verify browser permissions.");
}
);
}
// Geocoding world search
let searchDebounceTimer;
function searchNwiCities() {
clearTimeout(searchDebounceTimer);
const input = document.getElementById("nwi-search-input").value.trim();
const dropdown = document.getElementById("nwi-search-results");
if (input.length < 3) {
dropdown.style.display = "none";
return;
}
searchDebounceTimer = setTimeout(() => {
fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(input)}&count=5&language=en&format=json`)
.then(res => res.json())
.then(data => {
if (!data.results || data.results.length === 0) {
dropdown.innerHTML = '<div class="nwi-search-item">No locations found.</div>';
dropdown.style.display = "block";
return;
}
dropdown.innerHTML = "";
data.results.forEach(city => {
const div = document.createElement("div");
div.className = "nwi-search-item";
const state = city.admin1 ? `, ${city.admin1}` : "";
const country = city.country ? `, ${city.country}` : "";
const fullName = `${city.name}${state}${country}`;
div.innerText = fullName;
div.onclick = () => {
document.getElementById("nwi-search-input").value = city.name;
dropdown.style.display = "none";
// Set active to custom input state
document.querySelectorAll(".nwi-tab-btn").forEach(btn => btn.classList.remove("active"));
const lat = Math.round(city.latitude * 100) / 100;
const lon = Math.round(city.longitude * 100) / 100;
fetchNwiWeather(lat, lon, fullName);
};
dropdown.appendChild(div);
});
dropdown.style.display = "block";
})
.catch(err => {
console.error("Geocoding fetch error:", err);
});
}, 300);
}
function fetchNwiWeather(lat, lon, name) {
// Reset elements to loading states
document.getElementById("nwi-city-name").innerText = name;
document.getElementById("nwi-coords").innerText = `${lat}°N, ${lon}°W`;
document.getElementById("nwi-score-num").innerText = "-.-";
document.getElementById("nwi-classification-text").innerText = "Calculating...";
document.getElementById("nwi-summary-stats").innerText = "Connecting to Open-Meteo...";
document.getElementById("nwi-gauge-fill").style.strokeDashoffset = "339.29"; // 0 progress
const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode,dewpoint_2m_mean,wind_speed_10m_max&hourly=temperature_2m,relative_humidity_2m,dewpoint_2m,precipitation_probability,weathercode,wind_speed_10m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=auto&forecast_days=1`;
fetch(weatherUrl)
.then(res => {
if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
return res.json();
})
.then(data => {
renderNwiDashboard(data);
})
.catch(err => {
console.error("Open-Meteo connection error:", err);
document.getElementById("nwi-classification-text").innerText = "Connection Failed";
document.getElementById("nwi-summary-stats").innerHTML = `Unable to fetch live weather data: <span style="color: #ef4444; font-weight: bold;">${err.message}</span><br>Please verify your internet connection or check the browser console for details.`;
});
}
function renderNwiDashboard(data) {
try {
// Validate API structure
if (!data || !data.hourly || !data.daily) {
throw new Error(data?.reason || "Received an invalid or truncated dataset from Open-Meteo.");
}
const daily = data.daily;
const hourly = data.hourly;
// 1. Calculate Current Score with boundary checks
const hourlyLen = hourly.temperature_2m?.length || 0;
if (hourlyLen === 0) {
throw new Error("Hourly forecast data array is empty.");
}
const currentHour = Math.max(0, Math.min(new Date().getHours(), hourlyLen - 1));
const currentTemp = hourly.temperature_2m?.[currentHour] ?? 70;
const currentDewPoint = hourly.dewpoint_2m?.[currentHour] ?? 50;
const currentPrecipProb = hourly.precipitation_probability?.[currentHour] ?? 0;
const currentWindSpeed = hourly.wind_speed_10m?.[currentHour] ?? 5;
const currentWeatherCode = hourly.weathercode?.[currentHour] ?? 0;
const currentNwi = calculateNwiScore(currentTemp, currentDewPoint, currentPrecipProb, currentWindSpeed, currentWeatherCode);
const classification = getNwiClassification(currentNwi);
// Update Hero Gauge and Description
document.getElementById("nwi-score-num").innerText = currentNwi.toFixed(1);
const classTextEl = document.getElementById("nwi-classification-text");
classTextEl.innerText = `${classification.text}`;
classTextEl.className = `nwi-hero-meta h2 ${classification.class}`;
// Set Gauge SVG stroke
const fillEl = document.getElementById("nwi-gauge-fill");
fillEl.style.stroke = `url(#${classification.grad})`;
// Circular dash-array offset: 2 * PI * 54 = ~339.29
const offset = 339.29 - (339.29 * (currentNwi / 10));
fillEl.style.strokeDashoffset = offset;
fillEl.setAttribute("stroke-dashoffset", offset);
// Conditions Text Summary with safe defaults
const weatherText = getWeatherWmoText(currentWeatherCode);
const dailyTempMax = daily.temperature_2m_max?.[0] ?? 75;
const dailyTempMin = daily.temperature_2m_min?.[0] ?? 55;
const dailyWeatherCode = daily.weathercode?.[0] ?? 0;
const dailyPrecipProbMax = daily.precipitation_probability_max?.[0] ?? 0;
const dailyWeatherText = getWeatherWmoText(dailyWeatherCode);
document.getElementById("nwi-summary-stats").innerHTML = 
`Current: <strong>${Math.round(currentTemp)}°F</strong> | Dew Point: <strong>${Math.round(currentDewPoint)}°F</strong> | Wind: <strong>${Math.round(currentWindSpeed)} mph</strong><br>` +
`Sky: <strong>${weatherText}</strong> (Precip: <strong>${currentPrecipProb}%</strong>)<br>` +
`<span style="font-size: 0.85rem; opacity: 0.8;">Forecast: <strong>${Math.round(dailyTempMin)}°F to ${Math.round(dailyTempMax)}°F</strong> | Sky: <strong>${dailyWeatherText}</strong> (Max Precip: <strong>${dailyPrecipProbMax}%</strong>)</span>`;
// 2. Action Plan: Windows Advice
const windowsAdvice = calculateWindowsAdvice(hourly);
document.getElementById("nwi-advice-windows").innerHTML = windowsAdvice;
// Action Plan: Outdoor Advice
const outdoorAdvice = calculateOutdoorAdvice(hourly);
document.getElementById("nwi-advice-outdoors").innerHTML = outdoorAdvice;
// 3. Hourly Snapshot Cards (8am, 12pm, 4pm, 8pm)
const hours = [8, 12, 16, 20];
const hourIds = ["8a", "12p", "4p", "8p"];
hours.forEach((h, index) => {
const id = hourIds[index];
// Clamp snap hours within available response limits
const safeH = Math.min(h, hourlyLen - 1);
if (safeH < 0) return;
const t = hourly.temperature_2m?.[safeH] ?? 70;
const dp = hourly.dewpoint_2m?.[safeH] ?? 50;
const p = hourly.precipitation_probability?.[safeH] ?? 0;
const w = hourly.wind_speed_10m?.[safeH] ?? 5;
const wc = hourly.weathercode?.[safeH] ?? 0;
const hScore = calculateNwiScore(t, dp, p, w, wc);
const hClass = getNwiClassification(hScore);
const hText = getWeatherWmoText(wc);
const scoreEl = document.getElementById(`nwi-snap-score-${id}`);
scoreEl.innerText = hScore.toFixed(1);
scoreEl.className = `nwi-snap-score ${hClass.class}`;
document.getElementById(`nwi-snap-details-${id}`).innerHTML = 
`<strong>${Math.round(t)}°F</strong> | Dew: <strong>${Math.round(dp)}°F</strong><br>` +
`Wind: <strong>${Math.round(w)} mph</strong><br>` +
`<span style="color:#86868b">${hText} (${p}%)</span>`;
});
// 4. Render 24-Hour Timeline Chart
renderNwiTimeline(hourly);
} catch (err) {
console.error("Dashboard calculation error:", err);
document.getElementById("nwi-classification-text").innerText = "Calculation Error";
document.getElementById("nwi-summary-stats").innerHTML = 
`An error occurred while calculating weather indices: <span style="color: #ef4444; font-weight: bold;">${err.message}</span><br>` +
`<pre style="font-size: 0.75rem; text-align: left; background: rgba(0,0,0,0.05); padding: 0.5rem; border-radius: 8px; margin-top: 0.5rem; overflow-x: auto;">${err.stack}</pre>`;
}
}
function calculateWindowsAdvice(hourly) {
const comfortableHours = [];
let rainRisk = false;
let highHumid = false;
let tooCold = true;
let tooHot = true;
let tooWindy = true;
const len = Math.min(24, hourly.temperature_2m?.length || 0);
for (let i = 0; i < len; i++) {
const t = hourly.temperature_2m?.[i] ?? 70;
const dp = hourly.dewpoint_2m?.[i] ?? 50;
const p = hourly.precipitation_probability?.[i] ?? 0;
const w = hourly.wind_speed_10m?.[i] ?? 5;
const cTemp = t >= 60 && t <= 76;
const cDew = dp <= 56;
const cPrecip = p <= 15;
const cWind = w < 18;
if (cTemp && cDew && cPrecip && cWind) {
comfortableHours.push(i);
}
if (p > 15) rainRisk = true;
if (dp > 56) highHumid = true;
if (t >= 60) tooCold = false;
if (t <= 76) tooHot = false;
if (w < 18) tooWindy = false;
}
if (comfortableHours.length === 0) {
const reasons = [];
if (rainRisk) reasons.push("rain risk");
if (highHumid) reasons.push("high humidity");
if (tooCold) reasons.push("cool temperatures");
if (tooHot) reasons.push("warm/hot temperatures");
if (tooWindy) reasons.push("windy conditions");
let reasonStr = reasons.join(", ");
if (reasons.length > 1) {
const lastComma = reasonStr.lastIndexOf(", ");
reasonStr = reasonStr.substring(0, lastComma) + ", and " + reasonStr.substring(lastComma + 2);
}
return `<div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🚪 Windows Closed</div>` +
`<span style="color: #ef4444; font-weight: 700;">Keep windows closed today</span> due to ${reasonStr || "uncomfortable weather"}.`;
}
// Group into continuous ranges
const ranges = [];
let start = comfortableHours[0];
let prev = comfortableHours[0];
for (let i = 1; i < comfortableHours.length; i++) {
if (comfortableHours[i] === prev + 1) {
prev = comfortableHours[i];
} else {
ranges.push([start, prev]);
start = comfortableHours[i];
prev = comfortableHours[i];
}
}
ranges.push([start, prev]);
const rangeStrings = ranges.map(([s, e]) => `${formatHourAmPm(s)} – ${formatHourAmPm(e + 1 === 24 ? 23 : e + 1)}`);
return `<div style="font-size: 1.5rem; margin-bottom: 0.5rem; color: #10b981;">🚪 Windows Open</div>` +
`Ideal window hours today: <strong style="color: #10b981;">${rangeStrings.join(", ")}</strong>. Keep windows open during these times for crisp, comfortable indoor ventilation.`;
}
function calculateOutdoorAdvice(hourly) {
const hourlyScores = [];
let maxScore = 0;
const len = Math.min(24, hourly.temperature_2m?.length || 0);
for (let i = 0; i < len; i++) {
const t = hourly.temperature_2m?.[i] ?? 70;
const dp = hourly.dewpoint_2m?.[i] ?? 50;
const p = hourly.precipitation_probability?.[i] ?? 0;
const w = hourly.wind_speed_10m?.[i] ?? 5;
const wc = hourly.weathercode?.[i] ?? 0;
const score = calculateNwiScore(t, dp, p, w, wc);
hourlyScores.push({ hour: i, score });
if (score > maxScore) maxScore = score;
}
const threshold = maxScore >= 6.0 ? 6.0 : maxScore - 0.8;
const comfortableHours = hourlyScores.filter(h => h.score >= threshold).map(h => h.hour);
if (maxScore < 4.5) {
return `<div style="font-size: 1.5rem; margin-bottom: 0.5rem; color: #ef4444;">🌳 Outdoor Window</div>` +
`<span style="color: #ef4444; font-weight: 700;">No comfortable outdoor windows today</span> due to unpleasant weather. Keep outdoor plans short and stay comfortable inside.`;
}
if (comfortableHours.length === 0) {
return `<div style="font-size: 1.5rem; margin-bottom: 0.5rem; color: #0071e3;">🌳 Outdoor Window</div>` +
`No ideal outdoor windows today. Minimize outdoor activities if possible.`;
}
const ranges = [];
let start = comfortableHours[0];
let prev = comfortableHours[0];
for (let i = 1; i < comfortableHours.length; i++) {
if (comfortableHours[i] === prev + 1) {
prev = comfortableHours[i];
} else {
ranges.push([start, prev]);
start = comfortableHours[i];
prev = comfortableHours[i];
}
}
ranges.push([start, prev]);
const rangeStrings = ranges.map(([s, e]) => `${formatHourAmPm(s)} – ${formatHourAmPm(e + 1 === 24 ? 23 : e + 1)}`);
const statusColor = maxScore >= 7.5 ? '#3b82f6' : (maxScore >= 6.0 ? '#10b981' : '#6366f1');
const statusText = maxScore >= 7.5 ? 'Excellent outdoor hours' : (maxScore >= 6.0 ? 'Comfortable outdoor hours' : 'Best available times');
return `<div style="font-size: 1.5rem; margin-bottom: 0.5rem; color: ${statusColor};">🌳 Outdoor Window</div>` +
`Best times for outdoors today: <strong style="color: ${statusColor};">${rangeStrings.join(", ")}</strong>.<br>` +
`<span style="color: #86868b; font-size: 0.9rem;">(${statusText} with NWI scores peaking at <strong>${maxScore.toFixed(1)}/10</strong>)</span>`;
}
function renderNwiTimeline(hourly) {
const timelineEl = document.getElementById("nwi-hourly-timeline");
if (!timelineEl) return;
timelineEl.innerHTML = "";
const hourlyScores = [];
let maxScore = 0;
const len = Math.min(24, hourly.temperature_2m?.length || 0);
for (let i = 0; i < len; i++) {
const t = hourly.temperature_2m?.[i] ?? 70;
const dp = hourly.dewpoint_2m?.[i] ?? 50;
const p = hourly.precipitation_probability?.[i] ?? 0;
const w = hourly.wind_speed_10m?.[i] ?? 5;
const wc = hourly.weathercode?.[i] ?? 0;
const score = calculateNwiScore(t, dp, p, w, wc);
hourlyScores.push(score);
if (score > maxScore) maxScore = score;
}
const outdoorThreshold = maxScore >= 6.0 ? 6.0 : maxScore - 0.8;
const currentHour = new Date().getHours();
for (let i = 0; i < len; i++) {
const t = hourly.temperature_2m?.[i] ?? 70;
const dp = hourly.dewpoint_2m?.[i] ?? 50;
const p = hourly.precipitation_probability?.[i] ?? 0;
const w = hourly.wind_speed_10m?.[i] ?? 5;
const wc = hourly.weathercode?.[i] ?? 0;
const score = hourlyScores[i];
const isWindowComfortable = (t >= 60 && t <= 76) && (dp <= 56) && (p <= 15) && (w < 18);
const isOutdoorComfortable = (maxScore >= 4.5) && (score >= outdoorThreshold);
const classification = getNwiClassification(score);
const bgClass = "bg-" + classification.text.toLowerCase();
const formattedHour = formatHourAmPm(i);
const shortHour = formatHourShort(i);
const weatherText = getWeatherWmoText(wc);
const isCurrent = i === currentHour;
const col = document.createElement("div");
col.className = "nwi-timeline-column" + (isCurrent ? " current-hour" : "");
const heightPercent = score === 0 ? 3 : score * 10;
const tooltipContent = "<strong>" + formattedHour + (isCurrent ? " (Now)" : "") + "</strong><br>" +
"Comfort: <strong>" + score.toFixed(1) + "/10</strong> (" + classification.text + ")<br>" +
"Temp: <strong>" + Math.round(t) + "°F</strong> | Dew: <strong>" + Math.round(dp) + "°F</strong><br>" +
"Wind: <strong>" + Math.round(w) + " mph</strong> | Sky: <strong>" + weatherText + "</strong><br>" +
"Rain Prob: <strong>" + p + "%</strong>" +
(isWindowComfortable || isOutdoorComfortable ? (
"<div style='margin-top: 0.5rem; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 0.4rem; font-size: 0.75rem; display: flex; flex-direction: column; gap: 0.2rem;'>" +
(isWindowComfortable ? "<span style='color: #34d399;'>✅ Ideal window open hour</span>" : "") +
(isOutdoorComfortable ? "<span style='color: #60a5fa;'>🌳 Ideal outdoor hour</span>" : "") +
"</div>"
) : "");
col.innerHTML = "<div class='nwi-timeline-score-label'>" + score.toFixed(1) + "</div>" +
"<div class='nwi-timeline-bar-wrapper'>" +
"<div class='nwi-timeline-bar " + bgClass + "' style='height: " + heightPercent + "%'></div>" +
"</div>" +
"<div class='nwi-timeline-indicators'>" +
"<span class='nwi-indicator-dot " + (isWindowComfortable ? "active-window" : "") + "' title='" + (isWindowComfortable ? "Ideal Window Hour" : "") + "'></span>" +
"<span class='nwi-indicator-dot " + (isOutdoorComfortable ? "active-outdoor" : "") + "' title='" + (isOutdoorComfortable ? "Ideal Outdoor Hour" : "") + "'></span>" +
"</div>" +
"<div class='nwi-timeline-hour-label'>" + shortHour + "</div>";
col.addEventListener("mouseenter", function() {
const globalTooltip = document.getElementById("nwi-timeline-tooltip");
const card = document.querySelector(".nwi-timeline-card");
if (!globalTooltip || !card) return;
globalTooltip.innerHTML = tooltipContent;
const colRect = col.getBoundingClientRect();
const cardRect = card.getBoundingClientRect();
const x = colRect.left - cardRect.left + (colRect.width / 2);
const y = colRect.top - cardRect.top - 10;
globalTooltip.style.left = x + "px";
globalTooltip.style.top = y + "px";
globalTooltip.classList.add("visible");
});
col.addEventListener("mouseleave", function() {
const globalTooltip = document.getElementById("nwi-timeline-tooltip");
if (globalTooltip) globalTooltip.classList.remove("visible");
});
timelineEl.appendChild(col);
}
const scrollContainer = document.querySelector(".nwi-timeline-scroll-container");
if (scrollContainer) {
scrollContainer.addEventListener("scroll", function() {
const globalTooltip = document.getElementById("nwi-timeline-tooltip");
if (globalTooltip) globalTooltip.classList.remove("visible");
}, { passive: true });
}
}
function formatHourShort(h) {
if (h === 0) return "12a";
if (h === 12) return "12p";
if (h > 12) return `${h - 12}p`;
return `${h}a`;
}
</script>
