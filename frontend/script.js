async function searchWords() {
    const query = document.getElementById("search").value.trim();

    if (!query) {
        return;
    }

    const response = await fetch(
        `http://127.0.0.1:8000/search?q=${encodeURIComponent(query)}`
    );

    const words = await response.json();

    const results = document.getElementById("results");

    results.innerHTML = "";

    if (words.length === 0) {
        results.innerHTML = "<p>No results found.</p>";
        return;
    }

    for (const word of words) {
        let meaningsHTML = "";

        for (const meaning of word.meanings) {
            meaningsHTML += `<li>${meaning}</li>`;
        }

        let examplesHTML = "";

        for (const example of word.examples) {
            examplesHTML += `
                <div class="example">
                    <p><strong>${example.hanzi}</strong></p>
                    <p>${example.pinyin}</p>
                    <p>${example.english}</p>
                </div>
            `;
        }

        results.innerHTML += `
            <div class="result">
                <h2>${word.hanzi}</h2>

                <p class="pinyin">${word.pinyin}</p>

                <p>HSK ${word.hsk_level ?? "-"}</p>

                <h3>Meanings</h3>
                <ul>
                    ${meaningsHTML}
                </ul>

                <h3>Examples</h3>
                ${examplesHTML || "<p>No examples yet.</p>"}
            </div>
        `;
    }
}