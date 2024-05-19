document.addEventListener('DOMContentLoaded', function () {
    const problemItems = document.querySelectorAll('.problem-item');

    problemItems.forEach(item => {
        item.addEventListener('click', function () {
            const details = this.querySelector('.problem-details');
            details.classList.toggle('visible');
        });
    });
});

