(function() {
  var stored = localStorage.getItem('theme');
  if (stored) document.documentElement.setAttribute('data-theme', stored);

  function getTheme() {
    var attr = document.documentElement.getAttribute('data-theme');
    if (attr) return attr;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function updateIcon() {
    var btn = document.querySelector('.theme-toggle');
    if (!btn) return;
    btn.textContent = getTheme() === 'dark' ? '☀️' : '🌙';
  }

  document.addEventListener('DOMContentLoaded', function() {
    updateIcon();
    var btn = document.querySelector('.theme-toggle');
    if (btn) {
      btn.addEventListener('click', function() {
        var next = getTheme() === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        updateIcon();
      });
    }
  });

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function() {
    if (!localStorage.getItem('theme')) updateIcon();
  });
})();
