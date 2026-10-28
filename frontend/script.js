
const API_URL = "http://127.0.0.1:8000";

const searchInput = document.getElementById("search");
const resultsContainer = document.getElementById("results");

async function searchWords() {
    const query = searchInput.value.trim();

    if (!query) {
        resultsContainer.innerHTML =
            "<p>Please enter a word to search.</p>";
        return;
    }

    resultsContainer.innerHTML = "<p>Searching...</p>";

    try {
        const response = await fetch(
            `${API_URL}/search?q=${encodeURIComponent(query)}`
        );

        if (!response.ok) {
            throw new Error("Server error");
        }

        const words = await response.json();

        resultsContainer.innerHTML = "";

        if (words.length === 0) {
            resultsContainer.innerHTML =
                "<p>No results found.</p>";
            return;
        }

        for (const word of words) {
            const meaningsHTML = word.meanings
                .map(meaning => `<li>${meaning}</li>`)
                .join("");

            const examplesHTML = word.examples
                .map(example => `
                    <div class="example">
                        <p><strong>${example.hanzi}</strong></p>
                        <p>${example.pinyin}</p>
                        <p>${example.english}</p>
                    </div>
                `)
                .join("");

            resultsContainer.innerHTML += `
                <div class="result">
                    <h2>${word.hanzi}</h2>
                    <p class="pinyin">${word.pinyin}</p>
                    <p>HSK ${word.hsk_level ?? "-"}</p>

                    <h3>Meanings</h3>
                    <ul>${meaningsHTML}</ul>

                    <h3>Examples</h3>
                    ${examplesHTML || "<p>No examples yet.</p>"}
                </div>
            `;
        }
    } catch (error) {
        resultsContainer.innerHTML = `
            <p>Unable to connect to the dictionary server.
            Please try again later.</p>
        `;
        console.error(error);
    }
}

searchInput.addEventListener("keydown", event => {
    if (event.key === "Enter") {
        searchWords();
    }
});
