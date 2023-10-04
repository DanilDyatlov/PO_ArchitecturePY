# Принцип инверсии зависимостей (Dependency Inversion Principle – DIP) гласит, что классы должны зависеть от абстракций, а не от конкретных реализаций. 
# Высокоуровневые модули не должны зависеть от низкоуровневых модулей. Оба типа модулей должны зависеть от абстракций.

from abc import ABC, abstractmethod

# Баззовый класс интерфейс
class Notification(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

# Логика отправки уведомления по электронной почте. Реализующий интерфейс
class EmailSender(Notification):
    def send_notification(self, message):
        print(" Email notification: ", message)

# Класс User зависит от абстрактного метода Notification. 
# User принимает объект notification, который реализует интерфейс Notification. Мы можем передать различные реализации без изменении  User
# Если сделать зависимость между  User и реализации EmailSender - то будет ошибка принципа. 
class User:
    def __init__(self, username, email, notification: Notification):
        self.username = username
        self.email = email
        self.notification_service = notification

    def send_notification(self, message):
        self.notification_service.send_notification(message)

if __name__ == '__main__':
    email_sender = EmailSender()
    user = User("Андрюша", "andy@googly.com", email_sender)
    user.send_notification("Hello!")