import os

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from stdimage.models import StdImageField

# Create your models here.


class Tag(models.Model):
    """docstring: tags"""

    name = models.CharField(max_length=64)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """category model class"""

    name = models.CharField(max_length=64)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ContentMixin(models.Model):
    """base class for Post, Article and Documents"""

    title = models.CharField("Название", max_length=200)
    url_code = models.CharField(
        "Код ссылки", max_length=30, blank=True, default="НЕ УКАЗАН"
    )
    short_description = models.CharField("Краткое описание", max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="Тэги", blank=True)
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)
    created_date = models.DateTimeField("Дата создания", default=timezone.now)
    text = RichTextUploadingField(
        verbose_name="Текст",
        config_name="default",
        extra_plugins=["youtube"],
        external_plugin_resources=[
            (
                "youtube",
                "plugins/youtube/",
                # '/static_root/ckeditor/ckeditor/plugins/youtube/',
                # static/ckeditor_plugins/youtube/plugin.js
                "plugin.js",
            )
        ],
    )
    author = models.ForeignKey(
        "users.CustomUser", verbose_name="Автор", on_delete=models.CASCADE
    )

    publish_on_main_page = models.BooleanField(
        verbose_name="Опубликовать на главной", default=False
    )
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        abstract = True


class SidePanel(models.Model):
    title = models.CharField("Название", max_length=200)
    text = RichTextUploadingField(verbose_name="Текст")

    class Meta:
        verbose_name = "Боковая панель"
        verbose_name_plural = "Боковые панели"

    def __str__(self):
        return self.title


class Post(ContentMixin):
    """child of contentmixin"""

    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE, blank=True
    )
    publish_on_main_page = models.BooleanField(
        "Опубликовать на главной", null=True, default=False
    )
    publish_on_news_page = models.BooleanField(
        verbose_name="Опубликовать в ленте новостей", default=False
    )
    publish_in_basement = models.BooleanField(
        "Опубликовать в подвале на главной", default=False
    )
    side_panel = models.ForeignKey(
        SidePanel,
        verbose_name="Боковая панель",
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ["created_date"]
        get_latest_by = ["created_date"]
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def get_absolute_url(self):
        return reverse("details", kwargs={"content": "post", "pk": self.pk})

    def publish(self):
        """unused function"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Article(ContentMixin):
    """child of ContentMixin"""

    class Meta:
        ordering = ["created_date"]
        get_latest_by = ["created_date"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def publish(self):
        """unused, left for future"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        return self.title


class DocumentCategory(models.Model):
    name = models.CharField("Название категории", max_length=64)
    number = models.SmallIntegerField(
        verbose_name="Порядок сортировки", null=True, blank=True, default=None
    )
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Категория документа"
        verbose_name_plural = "Категории документов"

    def __str__(self):
        return self.name


class Document(models.Model):
    """ "
    эта модель используется для
    загрузки документов в базу данных
    """

    title = models.CharField("Название", max_length=500)
    document = models.FileField(
        verbose_name="Документ",
        upload_to="documents/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "docx", "doc", "jpg", "jpeg"],
                message="Неправильный тип файла, используйте\
                                        PDF, DOCX, DOC, JPG, JPEG",
            )
        ],
    )

    category = models.ForeignKey(
        DocumentCategory, blank=True, null=True, on_delete=models.SET_NULL
    )
    url_code = models.CharField(
        "Код ссылки", max_length=30, blank=True, default="НЕ УКАЗАН"
    )
    uploaded_at = models.DateTimeField(verbose_name="Загружен", default=timezone.now)
    tags = models.ManyToManyField(Tag, verbose_name="Тэги", blank=True)
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )
    post = models.ForeignKey(
        Post,
        verbose_name="Страница",
        blank=True,
        default="",
        on_delete=models.SET_NULL,
        null=True,
    )
    publish_on_main_page = models.BooleanField(
        verbose_name="Опубиковать на главной", default=False
    )
    publish_in_basement = models.BooleanField(
        verbose_name="Опубликовать в подвале", default=False
    )
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title

    def extension(self):
        name, extension = os.path.splitext(self.document.name)
        return extension


def get_image_filename():
    """unused function, left for future"""
    return "image_{}".format(slugify(timezone.now()))


class PostPhoto(models.Model):
    """model to load photos to content page"""

    post = models.ForeignKey(
        Post,
        verbose_name="новость",
        related_name="images",
        on_delete=models.SET_NULL,
        null=True,
    )
    image = models.ImageField("изображение", upload_to="upload/")
    title = models.CharField(
        "название", max_length=64, blank=True, default=get_image_filename
    )
    position = models.PositiveIntegerField("Позиция", default=0)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
        ordering = ["position"]

    def __str__(self):
        return "{} - {}".format(self.post, self.image)


class Message(models.Model):
    """this is the class to use within adapter patter realization"""

    STATUS_LIST = (
        (0, "new"),
        (1, "assigned"),
        (2, "notify_sent"),
        (3, "complete"),
    )
    title = models.CharField("Заголовок", max_length=64, blank=True)
    typeof = models.CharField("Тип сообщения", max_length=64, blank=True)
    params = models.CharField("Параметры сообщения", max_length=512, blank=True)
    sender_email = models.EmailField(
        "Адрес электронной почты", max_length=64, blank=True
    )
    sender_phone = models.CharField("Телефон", max_length=64, blank=True)
    created_date = models.DateTimeField("Дата получения", default=timezone.now)
    status = models.IntegerField("Статус", default=0, choices=STATUS_LIST)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.title

    def set_status(self, status_code):
        # if status_code in STATUS_LIST:
        self.status = status_code
        return "{} - {}".format(self.post, self.image)


class Contact(models.Model):
    title = models.CharField("Название контакта", max_length=64, blank=False)
    description = models.CharField("Описание", max_length=200, blank=False)
    email = models.EmailField("Адрес электронной почты", max_length=64, blank=False)
    phone = models.CharField("Телефон", max_length=64, blank=False)
    number = models.SmallIntegerField("Порядок вывода на сайт", default=0)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.title


class People(models.Model):
    photo = models.ImageField("Фотография", upload_to="uploads/", blank=True)
    name = models.CharField("ФИО", max_length=120, blank=False)
    job = models.CharField("Должность", max_length=120, blank=False)
    experience = models.CharField("Опыт работы", max_length=500, blank=True)
    ordering = models.SmallIntegerField("Ordering", default=0)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class Staff(People):
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Participant(People):
    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


class Menu(models.Model):
    """linking main page UI elements with its description"""

    url_code = models.CharField("Код ссылки", max_length=30)
    title = models.CharField("Заголовок ссылки", max_length=60)
    url = models.CharField("Адрес ссылки", max_length=200, default="НЕТ")
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    def __str__(self):
        return self.title


class Service(models.Model):
    """class for service template"""

    title = models.CharField(
        "Название услуги",
        max_length=64,
        help_text="""
            При добавлении услуги в этот раздел автоматически
            будет создан пункт меню в разделе "Услуги", в котором они
            сортируются в соответствии с порядком сортировки
        """,
    )
    short_description = models.CharField(
        "Краткое описание услуги", max_length=200, blank=True, null=True, default=None
    )
    pseudo = models.CharField("Псевдоним", max_length=30, default="pseudo")
    html = RichTextUploadingField("Описание услуги")
    number = models.SmallIntegerField(
        "Порядок сортировки", blank=True, null=True, default=None
    )
    bg_photo = models.ImageField(
        "Картинка для главной",
        upload_to="upload/",
        null=True,
        blank=True,
        default=None,
    )
    documents = models.ManyToManyField(Document, blank=True)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    disable_order_button = models.BooleanField(
        "Отключить кнопку подачи заявки", default=False
    )
    alternative_url = models.CharField(
        "Ссылка на другой раздел (не обязательно)",
        blank=True,
        null=True,
        max_length=100,
    )
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class Profile(models.Model):
    """class for templating organization"""

    org_logotype = models.ImageField(
        "Логотип организации", upload_to="upload/", blank=True, null=True, default=None
    )
    org_footer_logotype = models.ImageField(
        "Логотип для футера (необязательно)",
        upload_to="upload/",
        blank=True,
        null=True,
        default=None,
    )
    org_short_name = models.CharField(
        "Краткое название организации",
        max_length=100,
        blank=True,
        null=True,
        default=None,
    )
    org_full_name = models.CharField(
        "Полное название организации",
        max_length=300,
        blank=True,
        null=True,
        default=None,
    )
    org_intro = models.TextField(
        "Текст для главной страницы", blank=True, null=True, default=None
    )
    org_history = models.TextField(
        "История организаици", blank=True, null=True, default=None
    )
    # phone1 for header
    org_main_phone = models.CharField(
        "Главный телефон организации (используется в хедере)",
        max_length=200,
        blank=True,
        null=True,
        default=None,
    )
    org_main_phone_text = models.CharField(
        'Подпись под телефоном в хедере, например "Многоканальный"',
        max_length=200,
        blank=True,
        null=True,
        default=None,
    )
    # phone2 for header
    org_secondary_phone = models.CharField(
        "Второй телефон организации (используется в хедере)",
        max_length=200,
        blank=True,
        null=True,
        default=None,
    )
    org_secondary_phone_text = models.CharField(
        'Подпись под вторым телефоном в хедере, например "Бухгалтерия"',
        max_length=200,
        blank=True,
        null=True,
        default=None,
    )
    org_phones = models.TextField("Телефоны", blank=True, null=True, default=None)
    org_email = models.TextField(
        "Адрес электронной почты", blank=True, null=True, default=None
    )
    org_order_email = models.CharField(
        "Адреса для подключения формы заявки",
        max_length=100,
        blank=True,
        null=True,
        default=None,
    )
    org_header_emails = models.TextField(
        "Адреса электронной почты (для хедера)", blank=True, null=True, default=None
    )
    org_header_phones = models.TextField(
        "Телефоны (для хедера)", blank=True, null=True, default=None
    )
    org_address = models.TextField(
        "Адрес местоположения организации", null=True, blank=True, default=None
    )
    org_address_map_link = models.CharField(
        "Ссылка на карту", blank=True, null=True, default=None, max_length=500
    )
    org_work_time = models.CharField(
        "Время работы организации", null=True, blank=True, default=None, max_length=100
    )

    counterjs = models.TextField(blank=True, null=True, max_length=1500)
    counter_ID = models.CharField(
        "ID счетчика Яндекс.Метрики", blank=True, null=True, max_length=20
    )
    counter_js_goal1 = models.CharField(
        "JS код счетчика (1)", max_length=500, null=True, blank=True
    )
    counter_js_goal2 = models.CharField(
        "JS код счетчика (2)", max_length=500, null=True, blank=True
    )
    number = models.SmallIntegerField("Порядок сортировки", null=True, blank=True)
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Профиль организации"
        verbose_name_plural = "Профили организации"

    def __str__(self):
        return self.org_short_name


class Chunk(models.Model):
    """class for making html chunks on pages"""

    title = models.CharField("Название вставки", max_length=64)
    code = models.CharField(
        "Уникальный код вставки", max_length=64, default="КОД_ВСТАВКИ"
    )
    html = RichTextUploadingField("Форматирование вставки")

    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Вставка"
        verbose_name_plural = "Вставки"

    def __str__(self):
        return self.title


class Partner(models.Model):
    title = models.CharField("Название партнера", max_length=60)
    logo = models.ImageField("Логотип партнера", upload_to="upload/")
    number = models.SmallIntegerField("Порядок вывода на сайт")
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.title


class SlideBackgrounds(models.Model):
    title = models.CharField("Название", default="Слайдер", max_length=50)

    image = StdImageField(
        "Картинка для фона баннера",
        upload_to="backgrounds/",
        variations={
            "thumbnail": {"width": 200, "height": 100, "crop": True},
            "large": {"width": 1920, "height": 1080, "crop": True},
        },
    )
    activated = models.BooleanField("Активировать", null=True, default=False)
    short_description = models.TextField(
        "short description",
        max_length=500,
        null=True,
        blank=True,
    )
    related_post = models.ForeignKey(
        Post,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    related_post_button_name = models.CharField(max_length=50, default="Подробнее")
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Картинка для баннера"
        verbose_name_plural = "Картинки для баннера"

    def __str__(self):
        return self.title
