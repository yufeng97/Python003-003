学习笔记

##### 创建管理员账号

```bash
python manage.py createsuperuser
```

##### 使用 Form 对象定义表单

```python
# app/form.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)
```

```python
# app_name/views.py
from .from import LoginForm

login_form = LoginForm()

return render(request, 'demo.html', {form: login_form})
```

```html
<!-- app/templates/demo.html -->
<form action="/demo" method="post">
    {% csrf_token %}
    {{ form }}
</form>
```

##### 表单与 auth 功能结合

```python
# app/views.py
from django.contrib.auth import authenticate, login

if request.method == 'POST':
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        # 读取表单的返回值
        cd = login_form.cleaned_data 
        user = authenticate(username=cd['username'], password=cd['password'])
        if user:
            # 登陆用户
            login(request, user)  
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败')
```

### 生产环境部署

```bash
pip install gunicorn

gunicorn MyDjango.wsgi
```

