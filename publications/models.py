from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from stdimage import StdImageField

# Create your models here.


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
    tags = models.ManyToManyField("common.Tag", verbose_name="Тэги", blank=True)
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
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
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
        verbose_name="Side panel",
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ["created_date"]
        get_latest_by = ["created_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def get_absolute_url(self):
        return reverse("details", kwargs={"content": "post", "pk": self.pk})

    def publish(self):
        """unused function"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"Post: { self.title }"


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
        return f"Article: {self.title}"


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
    tags = models.ManyToManyField("common.Tag", verbose_name="Тэги", blank=True)
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
        related_name="photos",
        on_delete=models.SET_NULL,
        null=True,
    )
    image = models.ImageField(
        "изображение",
        upload_to="upload/",
    )
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


class Banner(models.Model):
    title = models.CharField("Название", default="Слайдер", max_length=50)

    image = StdImageField(
        "Фон баннера",
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
        "publications.Post",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    related_post_button_name = models.CharField(
        max_length=50,
        default="Подробнее",
    )
    number = models.SmallIntegerField(
        verbose_name="ordering",
        default=0,
    )
    json_data = models.JSONField("json-data", null=True, blank=True)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return self.title
