function burger() {
    var menuList = document.getElementById('menu-list');
    if (menuList.style.display === 'none' || menuList.style.display === '') {
        menuList.style.display = 'block';
    } else {
        menuList.style.display = 'none';
    }
}
function toggleStar(element) {
    element.classList.toggle('filled');
}


