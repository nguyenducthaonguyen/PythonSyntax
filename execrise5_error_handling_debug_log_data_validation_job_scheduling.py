def main():
    txt_begin = """
Trong phát triển phần mềm, đảm bảo tính ổn định, chính xác và hiệu quả của hệ thống là mục tiêu then chốt. \n
Để đạt được điều này, lập trình viên cần nắm vững và triển khai hiệu quả các kỹ thuật như xử lý lỗi, ghi log, xác thực dữ liệu, và lên lịch công việc.
"""

    txt_error_handling = """
Xử lý lỗi (Error Handling) là quá trình phát hiện, quản lý và phản hồi các lỗi xảy ra trong khi chương trình chạy. \n
Thay vì để chương trình bị dừng đột ngột, xử lý lỗi giúp hệ thống hoạt động ổn định hơn bằng cách dự đoán và xử lý các tình huống bất thường. Các kỹ thuật phổ biến bao gồm try-except trong Python hoặc try-catch trong Java. Một hệ thống có xử lý lỗi tốt sẽ giảm thiểu rủi ro và nâng cao trải nghiệm người dùng.
"""
    txt_logging = """
Ghi log gỡ lỗi (Debug Log) là một công cụ quan trọng giúp lập trình viên theo dõi hoạt động của ứng dụng trong thời gian thực. \n
Log giúp lưu lại thông tin về các sự kiện, lỗi, và trạng thái của hệ thống. \n
Việc sử dụng log đúng cách không chỉ hỗ trợ trong quá trình gỡ lỗi (debugging), mà còn trong giám sát và bảo trì hệ thống khi đã triển khai thực tế. \n
Mức độ log thường bao gồm: DEBUG, INFO, WARNING, ERROR, và CRITICAL.
"""
    txt_validate="""
Xác thực dữ liệu (Data Validation) đảm bảo rằng dữ liệu người dùng hoặc dữ liệu đầu vào phù hợp với định dạng và tiêu chuẩn mong muốn.  \n
Đây là lớp phòng thủ đầu tiên chống lại dữ liệu sai, lỗi logic hoặc thậm chí các cuộc tấn công như SQL injection. \n
Data validation có thể được thực hiện phía client, phía server, hoặc cả hai để tăng độ tin cậy.
"""
    txt_job_scheduling="""
Lên lịch công việc (Job Scheduling) là kỹ thuật quản lý các tác vụ định kỳ hoặc theo thời gian cụ thể. \n
Ví dụ, hệ thống có thể tự động gửi email báo cáo hàng ngày hoặc sao lưu dữ liệu mỗi đêm. \n
Trong Python, các thư viện như schedule, APScheduler, hoặc Celery giúp lập trình viên tổ chức và thực hiện các tác vụ tự động hiệu quả.
"""
    txt_end= """
Tóm lại, bốn yếu tố trên không chỉ là công cụ kỹ thuật, mà còn là biểu hiện của sự chuyên nghiệp và tính hệ thống trong phát triển phần mềm. \n
Khi được áp dụng đúng cách, chúng giúp tăng độ tin cậy, dễ bảo trì và bảo mật cho ứng dụng, đồng thời giảm thiểu rủi ro và lỗi trong quá trình vận hành.
"""
    print(txt_begin)
    print(txt_error_handling)
    print(txt_logging)
    print(txt_validate)
    print(txt_job_scheduling)
    print(txt_end)

if __name__ == "__main__":
    main()