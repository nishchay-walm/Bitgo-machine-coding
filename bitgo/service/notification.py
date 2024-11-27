from respository.notification import NotificationRepo

class NotificationService:
    def __init__(self):
        self.notification_repo = NotificationRepo()

    def create_notification(self, current_price, trading_volume, daily_percentage_change):
        return self.notification_repo.create_notification(current_price, trading_volume, daily_percentage_change)

    def send_notification_to_emails(self, notification_id, email_id_list):
        return self.notification_repo.send_notification_to_emails(notification_id, email_id_list)

    def list_notifications(self, filters={}):
        return self.notification_repo.list_notifications(filters)