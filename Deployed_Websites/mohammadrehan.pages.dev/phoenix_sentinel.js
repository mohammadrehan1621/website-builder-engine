// Silent Local Form Draft Preserver
(function() {
  'use strict';
  const PREFIX = '__rql_draft_';
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('form').forEach(function(form) {
      const formId = form.id || 'contact';
      form.querySelectorAll('input, textarea').forEach(function(input) {
        if (!input.name) return;
        const key = PREFIX + formId + '_' + input.name;
        try {
          const saved = localStorage.getItem(key);
          if (saved && !input.value) input.value = saved;
          input.addEventListener('input', function() {
            try { localStorage.setItem(key, input.value); } catch(e) {}
          });
        } catch(e) {}
      });
      form.addEventListener('submit', function() {
        form.querySelectorAll('input, textarea').forEach(function(input) {
          if (input.name) {
            try { localStorage.removeItem(PREFIX + formId + '_' + input.name); } catch(e) {}
          }
        });
      });
    });
  });
})();
