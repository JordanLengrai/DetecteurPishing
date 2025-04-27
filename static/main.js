document.getElementById('analyze-btn').onclick = async function() {
    const url = document.getElementById('input-url').value.trim();
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<span class="loader"></span> Analyse en cours...';
    resultDiv.className = 'result-card';
    if (!url) {
        resultDiv.innerHTML = '<span style="font-size:1.4em;">⚠️</span> Merci de saisir une URL ou un email.';
        resultDiv.className = 'result-card phishing';
        return;
    }
    try {
        const res = await fetch('/analyze', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({url})
        });
        const data = await res.json();
        if (data.phishing) {
            resultDiv.innerHTML = '<span style="font-size:1.7em;">🔴</span> <span><b>Attention</b> : ' + data.reason + '</span>';
            resultDiv.className = 'result-card phishing';
        } else {
            resultDiv.innerHTML = '<span style="font-size:1.7em;">🟢</span> <span><b>Sûr</b> : ' + data.reason + '</span>';
            resultDiv.className = 'result-card safe';
        }
        resultDiv.style.opacity = 0;
        setTimeout(() => { resultDiv.style.opacity = 1; }, 80);
    } catch (e) {
        resultDiv.innerHTML = '<span style="font-size:1.4em;">⚠️</span> Erreur lors de l’analyse.';
        resultDiv.className = 'result-card phishing';
    }
};
