var boxContainer = document.getElementsByTagName("a");
boxContainer.forEach(
    function cekurl(element) {
        if (this.href === window.location.href) {
            this.classList.add("active");
        }
    }
)