
گزارش پروژه

کلاس درس شامل نام، شناسه و تعداد واحد است. کلاس (person) شامل نام، سن و کدملیست کلاس (student) از کلاس شخص ارث‌ میگیره و شماره دانشجویی و فهرست نمرات را به آن اضافه می‌کند و توابعی برای ثبت نمره، محاسبه واحد، محاسبه معدل و نمایش کارنامه دارد. کلاس مدیریت هسته اصلی برنامه است و دانشجویان و درس‌ها را نگه می‌دارد و تمام عملیات اصلی مثل افزودن، حذف، ثبت نمره، مرتب‌سازی و آمار به کمک اون انجام میشه در برنامه از الگوریتم مرج سورت برای تمام سورت ها استفاده شده و پیچیدگیه زمانی هر عملیات و عملیات های آماری داخل کد پروژه به صورت کامنت موجوده

عملیات های موجود همراه با پیچیدگی زمانیشان:
(n = number of students and m = number of courses) 
(پیچیدگی زمانی هر عملیات رو به روی آن داخل پرانتز نوشته شده) 

add student (1) 
add course (1) 
remove student (1) 
add student grades (1) 
student info (1) 
student report (m)
sort students by name (nlog(n)) 
sort students by avrage grade (mn + nlog(n)) 
sort students by number of units (nm + nlog(n)) 
show student statistics (nm)
show students(n)
show courses(m)
