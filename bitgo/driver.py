from service.notification import NotificationService

if __name__ == "__main__":
    notification_service = NotificationService()
    
    #create a notification
    notification_1 = notification_service.create_notification(current_price=100, trading_volume=1000.1, daily_percentage_change=0.15)
    notification_2 = notification_service.create_notification(current_price=50, trading_volume=100.1, daily_percentage_change=0.25)

    # List notification
    filter_notification = notification_service.list_notifications({"current_price": 100})
    
 
    # Send Notification
    notification_service.send_notification_to_emails(notification_1.id, ["ajsrinivas@bitgo.com", "alokbaltiyal@bitgo.com"])