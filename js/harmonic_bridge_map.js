// Harmonic Bridge Map: Woodstone Festival
document.addEventListener('DOMContentLoaded', function() {
  const mapEl = document.getElementById('harmonic-bridge-map');
  if (!mapEl) return;
  // Festival Harmonics
  const harmonics = [
    { name: 'Presence', color: '#8FCB9B', desc: 'Being with, not over.' },
    { name: 'Accessibility', color: '#E4F4E0', desc: 'Welcoming every voice.' },
    { name: 'AI as Companion', color: '#3E4E2C', desc: 'Technology for dignity.' },
    { name: 'Seed-bringer', color: '#B5D99C', desc: 'Planting new truths.' }
  ];
  mapEl.innerHTML = harmonics.map(h =>
    `<div style="margin:8px 0;padding:8px 12px;background:${h.color};border-radius:8px;">
      <strong>${h.name}</strong>: ${h.desc}
    </div>`
  ).join('');
});
