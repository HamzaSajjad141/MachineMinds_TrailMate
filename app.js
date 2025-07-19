function handleSearch() {
  const location = document.getElementById("locationInput").value.trim();
  if (!location) {
    alert("Veuillez saisir un lieu.");
    return;
  }
  const categories = ["restaurant", "park", "museum", "beach", "shopping mall"];
  categories.forEach(category => {
    const query     = `best ${category}s in ${location}`;
    const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
    // on génère un nom unique pour chaque catégorie
    const windowName = `search_${category.replace(/\s+/g, '_')}`;
    window.open(searchUrl, windowName);
  });
}