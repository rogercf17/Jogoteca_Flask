document.getElementById('searchInput').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    const cards = document.querySelectorAll('.game-card');

    cards.forEach(card => {
        const name = card.dataset.name;
        const category = card.dataset.category;
        const console = card.dataset.console;

        if (name.includes(searchTerm) || category.includes(searchTerm) || console.includes(searchTerm)) {
            card.style.display = 'block';
        }else {
            card.style.display = 'none';
        }
    });
});
