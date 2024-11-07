function showNotification(type, message) {
    const container = document.getElementById('notifications-container');

    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.innerText = message;

    notification.onclick = function () {
        container.removeChild(notification);
    };

    container.appendChild(notification);

    setTimeout(() => {
        if (container.contains(notification)) {
            container.removeChild(notification);
        }
    }, 5000);
}