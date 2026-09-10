(() => {
  const form = document.getElementById('workshop-inquiry');
  if (!form) return;
  document.getElementById('inquiry-submit').hidden = false;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const body = ['John,', '',
      'Company or group: ' + data.get('company'),
      'Business questions: ' + data.get('needs'),
      'Preferred duration: ' + data.get('duration'),
      'Location: ' + data.get('location'),
      'Preferred timing: ' + data.get('timing')].join('\n');
    const url = 'mailto:john.schultz@grafeauction.com?subject=' +
      encodeURIComponent('Private workshop inquiry') + '&body=' + encodeURIComponent(body);
    document.getElementById('inquiry-status').textContent =
      'Your inquiry is ready for your mail app. Review and send it there. If it did not open, use the email link above.';
    window.location.href = url;
  });
})();
