from time import time
from models.notifications import Notification
from models.notification_delivery_task import NotificationDeliveryTask, NotificationDeliveryStatus

class NotificationRepo:
    def __init__(self):
        self.notification_list = []
        self.notification_delivery_task_list = []

    def __find_notification(self, filter):
        filtered_notification_list = []
        for notification in self.notification_list:
            match_found = True
            for k, v in filter.items():
                if k == "status":
                    if not self.__check_notification_has_status(notification, v):
                        match_found = False
                    continue
                elif getattr(notification, k) != v:
                    match_found = False
            if match_found:
                filtered_notification_list.append(notification)
        return filtered_notification_list
    
    def __process_notification_delivery_task(self, notification_delivery_task):
            try:
                # Add logic to send email notification here
                print("Sending email to " + notification_delivery_task.email_id)
                notification_delivery_task.status = NotificationDeliveryStatus.SENT
                notification_delivery_task.delivered_at = time()
            except Exception as e:
                print("Exception in sending email = ", e)
                notification_delivery_task.status = NotificationDeliveryStatus.PENDING



    def create_notification(self, current_price, trading_volume, daily_percentage_change):
        notification = Notification(current_price=current_price, trading_volume=trading_volume, daily_percentage_change=daily_percentage_change)
        self.notification_list.append(notification)
        return notification
    
    def send_notification_to_emails(self, notification_id, email_id_list):
        filtered_notification_list = self.__find_notification({"id": notification_id})
        notification = None
        if len(filtered_notification_list)>0:
            notification = filtered_notification_list[0]
        else:
            raise Exception("Notification not found")
        
        for email_id in email_id_list:
            notification_delivery_task = NotificationDeliveryTask(notification=notification, email_id=email_id)
            self.notification_delivery_task_list.append(notification_delivery_task)
            self.__process_notification_delivery_task(notification_delivery_task)
    
    def __check_notification_has_status(self, notification, notification_status):
        notification_set = set()
        for notification_delivery_task in self.notification_delivery_task_list:
            if notification_delivery_task.status.val == notification_status:
                notification_set.add(notification_delivery_task.notification.id)
        return notification.id in notification_set  
    
    def list_notifications(self, filter):
        return self.__find_notification(filter) 
        
    