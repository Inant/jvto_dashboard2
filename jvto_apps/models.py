# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Activities(models.Model):
    id = models.BigAutoField(primary_key=True)
    activity_category = models.ForeignKey('ActivityCategories', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activities'


class ActivityCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_categories'


class ActivityEnds(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    d = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_ends'


class ActivityStarts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    destination = models.ForeignKey('Destinations', models.DO_NOTHING, blank=True, null=True)
    b = models.CharField(max_length=1)
    l = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_starts'


class AddOnCarts(models.Model):
    id = models.BigAutoField(primary_key=True)
    cart = models.ForeignKey('Carts', models.DO_NOTHING)
    add_on = models.ForeignKey('AddOns', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_on_carts'


class AddOnPackages(models.Model):
    id = models.BigAutoField(primary_key=True)
    add_on = models.ForeignKey('AddOns', models.DO_NOTHING)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_on_packages'


class AddOns(models.Model):
    id = models.BigAutoField(primary_key=True)
    add_on = models.CharField(max_length=255)
    is_transport = models.CharField(max_length=1)
    type_transport = models.CharField(max_length=6, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_ons'


class Agents(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    booking_code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    long_name = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agents'


class Announcements(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    cover = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcements'


class Areas(models.Model):
    id = models.BigAutoField(primary_key=True)
    area_name = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_start = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'


class AttachmentTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachment_types'


class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    banner = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=7)
    views = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs'


class BookActivities(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    day = models.IntegerField()
    date = models.DateField()
    activity = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_activities'


class BookAddOns(models.Model):
    id = models.BigAutoField(primary_key=True)
    add_on_package = models.ForeignKey(AddOnPackages, models.DO_NOTHING, blank=True, null=True)
    add_on = models.ForeignKey(AddOns, models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING, blank=True, null=True)
    price = models.FloatField()
    qty = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_add_ons'


class BookAttachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_attachments'


class BookCars(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING, blank=True, null=True)
    car = models.ForeignKey('Cars', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    driver_id = models.PositiveBigIntegerField(blank=True, null=True)
    total_rent = models.IntegerField(blank=True, null=True)
    total_fuel = models.IntegerField(blank=True, null=True)
    total_fee_driver = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_cars'


class BookGuideDrivers(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    guide = models.ForeignKey('GuideDrivers', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=6, blank=True, null=True)
    guide_type = models.CharField(max_length=9, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True, db_comment='Duration in days')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    guide_ijen = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'book_guide_drivers'


class BookHotelService(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_room_hotel = models.ForeignKey('BookRoomHotels', models.DO_NOTHING, blank=True, null=True)
    hotel_service = models.ForeignKey('HotelServices', models.DO_NOTHING, blank=True, null=True)
    qty = models.IntegerField()
    subtotal = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_hotel_service'


class BookHotels(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING, blank=True, null=True)
    booking_itinerary = models.ForeignKey('BookingItineraries', models.DO_NOTHING)
    hotel = models.ForeignKey('Hotels', models.DO_NOTHING, blank=True, null=True)
    b = models.CharField(max_length=1)
    l = models.CharField(max_length=1)
    d = models.CharField(max_length=1)
    remarks = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True, db_comment='0=reject, 1=approve')
    reject_msg = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_hotels'


class BookItineraries(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING, blank=True, null=True)
    day = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    start_area_id = models.PositiveBigIntegerField(blank=True, null=True)
    end_area_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_itineraries'


class BookItineraryDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_itinerary = models.ForeignKey(BookItineraries, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    destination = models.ForeignKey('Destinations', models.DO_NOTHING, blank=True, null=True)
    is_start = models.IntegerField(blank=True, null=True, db_comment='Jika start maka 1, jika end maka null atau 0 dan is end nya 1')
    is_end = models.IntegerField(blank=True, null=True, db_comment='Jika end maka 1, jika start maka null atau 0 dan is start nya 1')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_itinerary_details'


class BookJeeps(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    hotel = models.ForeignKey('Hotels', models.DO_NOTHING, blank=True, null=True)
    hotel_check_in = models.DateField(blank=True, null=True)
    qty_jeep = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_jeeps'


class BookMeals(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    day = models.IntegerField()
    date = models.DateField()
    breakfast = models.CharField(max_length=1)
    lunch = models.CharField(max_length=1)
    dinner = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_meals'


class BookRoomHotels(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    booking_itinerary = models.ForeignKey('BookingItineraries', models.DO_NOTHING, blank=True, null=True)
    book_hotel = models.ForeignKey(BookHotels, models.DO_NOTHING, blank=True, null=True)
    room_hotel = models.ForeignKey('RoomHotels', models.DO_NOTHING)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    day = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    hotel_id = models.PositiveBigIntegerField(blank=True, null=True)
    double = models.IntegerField(blank=True, null=True)
    twin = models.IntegerField(blank=True, null=True)
    extra_bed = models.IntegerField(blank=True, null=True)
    capsule = models.IntegerField(blank=True, null=True)
    subtotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_room_hotels'


class BookServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    service = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    other_service = models.CharField(max_length=255, blank=True, null=True, db_comment='For other service which not listed on services')
    day = models.PositiveIntegerField()
    date = models.DateField()
    qty = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    guide_ijen = models.ForeignKey('GuideDrivers', models.DO_NOTHING, blank=True, null=True)
    subtotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_services'


class BookingAdditionalPriceBookings(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    item = models.CharField(max_length=255)
    quantity = models.FloatField()
    price = models.FloatField()
    subtotal = models.FloatField()
    attachment = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_additional_price_bookings'


class BookingCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    agent = models.ForeignKey(Agents, models.DO_NOTHING)
    is_transport = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_categories'


class BookingDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING, blank=True, null=True)
    price_plan = models.ForeignKey('PricePlans', models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    travel_date_start = models.DateField()
    travel_date_end = models.DateField()
    pax = models.IntegerField()
    xss = models.PositiveIntegerField(blank=True, null=True)
    xxs = models.IntegerField(blank=True, null=True)
    xs = models.IntegerField(blank=True, null=True)
    s = models.IntegerField()
    m = models.IntegerField()
    l = models.IntegerField()
    xl = models.IntegerField()
    xxl = models.IntegerField()
    xxxl = models.IntegerField(blank=True, null=True)
    custom_tshirt = models.CharField(max_length=255, blank=True, null=True)
    custom_tshirt_note = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1)
    total = models.FloatField()
    request_schedule = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_details'


class BookingDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    attachment_type = models.ForeignKey(AttachmentTypes, models.DO_NOTHING)
    file = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_documents'


class BookingItineraries(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking_id = models.PositiveBigIntegerField()
    day = models.IntegerField()
    activity_start = models.ForeignKey(ActivityStarts, models.DO_NOTHING, blank=True, null=True)
    activity_end = models.ForeignKey(ActivityEnds, models.DO_NOTHING, blank=True, null=True)
    itinerary = models.CharField(max_length=255)
    activity = models.TextField(blank=True, null=True)
    b = models.CharField(max_length=1, blank=True, null=True)
    l = models.CharField(max_length=1, blank=True, null=True)
    d = models.CharField(max_length=1, blank=True, null=True)
    accommodation = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_itineraries'


class BookingPayments(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    nominal = models.FloatField()
    payment_method = models.ForeignKey('PaymentMethods', models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_payments'


class BookingRefundAndPenalties(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    item = models.CharField(max_length=255)
    quantity = models.FloatField()
    price = models.FloatField()
    subtotal = models.FloatField()
    attachment = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_refund_and_penalties'


class BookingReviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    trip_rate = models.IntegerField(blank=True, null=True)
    package_rate = models.IntegerField(blank=True, null=True)
    package_feedback = models.TextField(blank=True, null=True)
    crew_feedback = models.TextField(blank=True, null=True)
    know_from = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_reviews'


class Bookings(models.Model):
    id = models.BigAutoField(primary_key=True)
    trip_name = models.CharField(max_length=255, blank=True, null=True)
    booking_code_app = models.CharField(max_length=255, blank=True, null=True)
    booking_code = models.CharField(max_length=255)
    invoice_code_origin = models.CharField(max_length=255, blank=True, null=True)
    booking_category = models.ForeignKey(BookingCategories, models.DO_NOTHING, blank=True, null=True)
    booking_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    hotel_id_transport = models.ForeignKey('Hotels', models.DO_NOTHING, db_column='hotel_id_transport', blank=True, null=True)
    booking_numb = models.CharField(max_length=255, blank=True, null=True)
    booking_from = models.CharField(max_length=255, blank=True, null=True)
    inclusion = models.TextField(blank=True, null=True)
    exclusion = models.TextField(blank=True, null=True)
    no_st = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    travel_date_start = models.DateField(blank=True, null=True)
    travel_date_end = models.DateField(blank=True, null=True)
    total_pax = models.FloatField()
    dp = models.FloatField()
    dp_no_idr = models.FloatField()
    currency = models.CharField(max_length=255, blank=True, null=True)
    add_on_total = models.FloatField()
    discount = models.ForeignKey('Discounts', models.DO_NOTHING, blank=True, null=True)
    discount_type = models.CharField(max_length=7, blank=True, null=True)
    referral_code = models.CharField(max_length=255, blank=True, null=True, db_comment='referral code from referrer')
    discount_percent = models.IntegerField(blank=True, null=True, db_comment='discount in percentage')
    discount_0 = models.FloatField(db_column='discount', blank=True, null=True)  # Field renamed because of name conflict.
    grand_total_before_disc = models.FloatField(blank=True, null=True)
    deposit = models.CharField(max_length=10, blank=True, null=True)
    grand_total = models.FloatField()
    payment_status = models.CharField(max_length=8)
    debt = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=17, blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)
    payment_method = models.CharField(max_length=9, blank=True, null=True)
    payment_link = models.CharField(max_length=255, blank=True, null=True)
    outstanding_payment_method = models.CharField(max_length=4, blank=True, null=True)
    outstanding_payment_link = models.CharField(max_length=255, blank=True, null=True)
    meeting_point = models.CharField(max_length=255, blank=True, null=True)
    surabaya_hotel = models.CharField(max_length=255, blank=True, null=True)
    special_requirements = models.CharField(max_length=255, blank=True, null=True)
    flight_ticket = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    terminal_flight_code = models.CharField(max_length=255, blank=True, null=True)
    flight_from = models.CharField(max_length=255, blank=True, null=True)
    flight_to = models.CharField(max_length=255, blank=True, null=True)
    departure = models.CharField(max_length=255, blank=True, null=True)
    departure_time = models.TimeField(blank=True, null=True)
    pickup_note = models.CharField(max_length=255, blank=True, null=True)
    pickup = models.CharField(max_length=255, blank=True, null=True)
    ticket_type_number = models.CharField(max_length=255, blank=True, null=True)
    pickup_time = models.TimeField(blank=True, null=True)
    drop = models.CharField(max_length=255, blank=True, null=True)
    drop_time = models.TimeField(blank=True, null=True)
    student_card = models.CharField(max_length=255, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    margin = models.FloatField(blank=True, null=True)
    mr_sam = models.FloatField(blank=True, null=True)
    reject_pay_later_msg = models.TextField(blank=True, null=True)
    whatsapp_sended = models.IntegerField()
    media_link = models.TextField(blank=True, null=True)
    is_window = models.CharField(max_length=1, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    is_police_escort = models.CharField(max_length=1, blank=True, null=True)
    police_escort_pickup_date = models.DateTimeField(blank=True, null=True)
    police_escort_route = models.CharField(max_length=255, blank=True, null=True)
    url_name = models.CharField(max_length=255, blank=True, null=True)
    pickup_sign = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    surat_tugas_file = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)
    package_duration = models.IntegerField(blank=True, null=True, db_comment='Package duration in days')
    template_package = models.ForeignKey('Packages', models.DO_NOTHING, blank=True, null=True)
    bromo_hotel = models.ForeignKey('Hotels', models.DO_NOTHING, related_name='bookings_bromo_hotel_set', blank=True, null=True)
    bromo_hotel_checkin = models.DateField(blank=True, null=True)
    qty_jeep = models.IntegerField(blank=True, null=True)
    is_share_media = models.CharField(max_length=1)
    is_shuttle = models.CharField(max_length=1)
    at_bondowoso = models.DateField(blank=True, null=True)
    at_bromo = models.DateField(blank=True, null=True)
    is_send_wa = models.CharField(max_length=1, db_comment='send wa during the trip or not')
    wa_status_trip_information = models.CharField(max_length=2, db_comment='0:Belum,00:Gagal,1:Sukses')
    wa_schedule_trip_information = models.DateTimeField(blank=True, null=True)
    wa_status_trip_media = models.CharField(max_length=2, db_comment='0:Belum,00:Gagal,1:Sukses')
    wa_schedule_trip_media = models.DateTimeField(blank=True, null=True)
    wa_status_trip_media_crew = models.CharField(max_length=2, db_comment='0:Belum,00:Gagal,1:Sukses')
    wa_schedule_trip_media_crew = models.DateTimeField(blank=True, null=True)
    wa_status_trip_itinerary_crew = models.CharField(max_length=2, db_comment='0:Belum,00:Gagal,1:Sukses')
    wa_status_at_bondowoso_crew = models.CharField(max_length=2, db_comment='0:Belum,00:Gagal,1:Sukses')
    wa_status_at_bromo_crew = models.CharField(max_length=2, db_comment='0:Belum,00:Gagal,1:Sukses')
    wa_schedule_payment_content = models.TextField(blank=True, null=True)
    expense_file = models.CharField(max_length=255, blank=True, null=True)
    expense_file_internal = models.CharField(max_length=255, blank=True, null=True)
    expense_total = models.FloatField(blank=True, null=True)
    expense_internal_total = models.FloatField()
    income = models.FloatField()
    is_invoiced_twt = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'bookings'


class CalculationDetailOthers(models.Model):
    id = models.BigAutoField(primary_key=True)
    calculation = models.ForeignKey('Calculations', models.DO_NOTHING)
    item = models.ForeignKey('ItemCalculationOthers', models.DO_NOTHING)
    qty = models.FloatField()
    amount = models.FloatField(blank=True, null=True)
    rent = models.FloatField(blank=True, null=True)
    fuel = models.FloatField(blank=True, null=True)
    driver = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField()
    type = models.CharField(max_length=9)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calculation_detail_others'


class CalculationDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    calculation = models.ForeignKey('Calculations', models.DO_NOTHING)
    item = models.ForeignKey('ItemCalculations', models.DO_NOTHING)
    amount = models.FloatField()
    qty = models.FloatField()
    subtotal = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calculation_details'


class Calculations(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING, blank=True, null=True)
    booking_total = models.FloatField()
    calculation_total = models.FloatField()
    profit = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calculations'


class Cars(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    car_name = models.CharField(max_length=255, blank=True, null=True)
    garage = models.ForeignKey('Garages', models.DO_NOTHING, blank=True, null=True)
    banner = models.CharField(max_length=255, blank=True, null=True)
    start_pax = models.IntegerField(blank=True, null=True)
    end_pax = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fuel = models.FloatField(blank=True, null=True)
    driver = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    interior = models.CharField(max_length=255, blank=True, null=True)
    interior_3d = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_publish = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cars'


class Carts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    package_price = models.ForeignKey('PackagePrices', models.DO_NOTHING)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    travel_date = models.DateField()
    pax = models.IntegerField()
    s = models.IntegerField(blank=True, null=True)
    m = models.IntegerField(blank=True, null=True)
    l = models.IntegerField(blank=True, null=True)
    xl = models.IntegerField(blank=True, null=True)
    xxl = models.IntegerField(blank=True, null=True)
    total = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carts'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class ComponentContents(models.Model):
    id = models.BigAutoField(primary_key=True)
    component = models.ForeignKey('Components', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    content = models.TextField()
    page_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component_contents'


class Components(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    component_name = models.CharField(max_length=255)
    preview = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'components'


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    short_name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    dial_code = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class CrewReviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking_review = models.ForeignKey(BookingReviews, models.DO_NOTHING)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    crew = models.ForeignKey('GuideDrivers', models.DO_NOTHING)
    rate = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crew_reviews'


class CurrencyExchange(models.Model):
    id = models.BigAutoField(primary_key=True)
    currency_code = models.CharField(max_length=255)
    conversion_rates = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency_exchange'


class Destinations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    elevation_gain = models.FloatField(blank=True, null=True)
    route_type = models.CharField(max_length=255, blank=True, null=True)
    img_map = models.CharField(max_length=255, blank=True, null=True)
    trek_video = models.CharField(max_length=255, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    alltrails_map = models.TextField(blank=True, null=True)
    gallery = models.ForeignKey('Galleries', models.DO_NOTHING)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField()
    calculation_order = models.IntegerField(blank=True, null=True)
    is_publish = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    area_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'destinations'


class Discounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gift_card = models.ForeignKey('GiftCards', models.DO_NOTHING, blank=True, null=True)
    disc = models.FloatField()
    type = models.CharField(max_length=7)
    email = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING, blank=True, null=True)
    valid_until = models.DateField(blank=True, null=True)
    verification_code = models.CharField(max_length=255, blank=True, null=True)
    is_verif = models.CharField(max_length=1)
    is_used = models.CharField(max_length=1)
    is_isic = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discounts'


class DocumentFinders(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_finders'


class Durations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    day = models.IntegerField()
    night = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'durations'


class EmailAccounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    username = models.CharField(max_length=255, blank=True, null=True)
    from_name = models.CharField(max_length=255, blank=True, null=True)
    reply_to_mail = models.CharField(max_length=255, blank=True, null=True)
    reply_to_name = models.CharField(max_length=255, blank=True, null=True)
    provider = models.ForeignKey('EmailProviders', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_accounts'


class EmailProviders(models.Model):
    id = models.BigAutoField(primary_key=True)
    host = models.CharField(max_length=255)
    port = models.CharField(max_length=255)
    encryption = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_providers'


class Experiences(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    background = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiences'


class ExtraLuggages(models.Model):
    id = models.BigAutoField(primary_key=True)
    price_maker = models.ForeignKey('PriceMakers', models.DO_NOTHING, blank=True, null=True)
    extra_luggage = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extra_luggages'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class FaqCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faq_categories'


class FaqSubcategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    faq_category = models.ForeignKey(FaqCategories, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faq_subcategories'


class Faqs(models.Model):
    id = models.BigAutoField(primary_key=True)
    faq_category = models.ForeignKey(FaqCategories, models.DO_NOTHING)
    faq_subcategory = models.ForeignKey(FaqSubcategories, models.DO_NOTHING, blank=True, null=True)
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faqs'


class Galleries(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=255)
    og_image = models.CharField(max_length=255, blank=True, null=True)
    destination = models.ForeignKey(Destinations, models.DO_NOTHING, blank=True, null=True)
    caption = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'galleries'


class Garages(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    background = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garages'


class GiftCards(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gift_cards'


class GroupUser(models.Model):
    user_id = models.IntegerField()
    group_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'group_user'


class GuideDrivers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    crew_level = models.CharField(max_length=6, blank=True, null=True)
    crew_id = models.IntegerField(blank=True, null=True)
    garage = models.ForeignKey(Garages, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    device_token = models.TextField(blank=True, null=True)
    fcm_token = models.TextField(blank=True, null=True)
    is_driver = models.IntegerField()
    is_ijen = models.IntegerField()
    crew_photo = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    star = models.FloatField(blank=True, null=True)
    guide_license = models.CharField(max_length=255, blank=True, null=True)
    driver_license = models.CharField(max_length=255, blank=True, null=True)
    ktp = models.CharField(max_length=255, blank=True, null=True)
    id_card = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=255)
    new_role = models.CharField(max_length=255, blank=True, null=True, db_comment='kolom untuk kategori role baru')
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guide_drivers'


class HotelServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    hotel = models.ForeignKey('Hotels', models.DO_NOTHING)
    service = models.CharField(max_length=255)
    rate = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_services'


class Hotels(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    destination = models.ForeignKey(Destinations, models.DO_NOTHING, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    booking_code = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    banner = models.CharField(max_length=255, blank=True, null=True)
    map_url = models.TextField(blank=True, null=True)
    lunch_rate = models.FloatField(blank=True, null=True)
    dinner_rate = models.FloatField(blank=True, null=True)
    is_publish = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    area2 = models.ForeignKey(Areas, models.DO_NOTHING, related_name='hotels_area2_set', blank=True, null=True)
    double_rate = models.IntegerField(blank=True, null=True)
    twin_rate = models.IntegerField(blank=True, null=True)
    extra_bed_rate = models.IntegerField(blank=True, null=True)
    capsule_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotels'


class IdentitiesTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'identities_types'


class IdentityCards(models.Model):
    id = models.BigAutoField(primary_key=True)
    guide_driver = models.ForeignKey(GuideDrivers, models.DO_NOTHING)
    identity_type = models.ForeignKey(IdentitiesTypes, models.DO_NOTHING)
    front_file = models.CharField(max_length=255)
    back_file = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'identity_cards'


class ImagePanoramas(models.Model):
    id = models.BigAutoField(primary_key=True)
    destination = models.ForeignKey(Destinations, models.DO_NOTHING)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_panoramas'


class IncludeExcludes(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    type = models.CharField(max_length=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'include_excludes'


class InvoiceHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    description = models.CharField(max_length=255)
    rate = models.FloatField()
    qty = models.IntegerField()
    line_total = models.FloatField()
    type = models.CharField(max_length=255)
    parent_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_histories'


class InvoiceTwtDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_twt = models.ForeignKey('InvoiceTwts', models.DO_NOTHING)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_twt_details'


class InvoiceTwts(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_no = models.CharField(max_length=255)
    invoice_date = models.DateField()
    status = models.CharField(max_length=6)
    total = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_twts'


class ItemCalculationOthers(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.CharField(max_length=255)
    rent = models.FloatField(blank=True, null=True)
    fuel = models.FloatField(blank=True, null=True)
    driver = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=9, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_calculation_others'


class ItemCalculations(models.Model):
    id = models.BigAutoField(primary_key=True)
    destination = models.ForeignKey(Destinations, models.DO_NOTHING, blank=True, null=True)
    item = models.CharField(max_length=255, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_calculations'


class Itineraries(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    day = models.IntegerField()
    activity_start = models.ForeignKey(ActivityStarts, models.DO_NOTHING, blank=True, null=True)
    activity_end = models.ForeignKey(ActivityEnds, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    activity = models.TextField()
    short_activity = models.TextField(blank=True, null=True)
    guide_book = models.TextField(blank=True, null=True)
    b = models.CharField(max_length=1)
    l = models.CharField(max_length=1)
    d = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itineraries'


class ItineraryDestinations(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    itinerary = models.ForeignKey(Itineraries, models.DO_NOTHING)
    destination = models.ForeignKey(Destinations, models.DO_NOTHING)
    second_destination = models.ForeignKey(Destinations, models.DO_NOTHING, related_name='itinerarydestinations_second_destination_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itinerary_destinations'


class ItineraryDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    itinerary = models.ForeignKey(Itineraries, models.DO_NOTHING)
    time = models.TimeField(blank=True, null=True)
    activity = models.ForeignKey(Activities, models.DO_NOTHING)
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itinerary_details'


class ItineraryInvoices(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    activity = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itinerary_invoices'


class ItineraryMeals(models.Model):
    id = models.BigAutoField(primary_key=True)
    itinerary = models.ForeignKey(Itineraries, models.DO_NOTHING)
    price_plan = models.ForeignKey('PricePlans', models.DO_NOTHING)
    breakfast = models.CharField(max_length=1)
    lunch = models.CharField(max_length=1)
    dinner = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itinerary_meals'


class JvtoReviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    date = models.DateField()
    star = models.FloatField()
    review = models.TextField()
    photos = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jvto_reviews'


class Links(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    short_url = models.CharField(max_length=255)
    file = models.TextField()
    type = models.CharField(max_length=4)
    is_publish = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'links'


class Locations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    map = models.TextField(blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class MiceForms(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    company_website = models.CharField(max_length=255, blank=True, null=True)
    company_location = models.CharField(max_length=255, blank=True, null=True)
    attendees = models.CharField(max_length=255, blank=True, null=True)
    destinations = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mice_forms'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class OrderChannels(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_channels'


class PackageActivities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_activities'


class PackageBanners(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    gallery = models.ForeignKey(Galleries, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_banners'


class PackageCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    banner = models.CharField(max_length=255)
    banner_full = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_categories'


class PackageDestinations(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    destination = models.ForeignKey(Destinations, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_destinations'


class PackageHotels(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    price_plan = models.ForeignKey('PricePlans', models.DO_NOTHING, blank=True, null=True)
    hotel = models.ForeignKey(Hotels, models.DO_NOTHING)
    room_name = models.CharField(max_length=255, blank=True, null=True)
    day = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_hotels'


class PackageIncludeExcludes(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    include_exclude = models.ForeignKey(IncludeExcludes, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_include_excludes'


class PackageMeals(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    price_plan = models.ForeignKey('PricePlans', models.DO_NOTHING)
    breakfast = models.IntegerField()
    lunch = models.IntegerField()
    dinner = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_meals'


class PackagePrices(models.Model):
    id = models.BigAutoField(primary_key=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    price_plan = models.ForeignKey('PricePlans', models.DO_NOTHING, blank=True, null=True)
    price_category = models.ForeignKey('PriceCategories', models.DO_NOTHING)
    price = models.FloatField()
    price_before_disc = models.FloatField()
    disc_percent = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_prices'


class PackageTransportations(models.Model):
    id = models.BigAutoField(primary_key=True)
    price_plan = models.ForeignKey('PricePlans', models.DO_NOTHING)
    transportation = models.ForeignKey(Cars, models.DO_NOTHING)
    start_pax = models.IntegerField()
    end_pax = models.IntegerField(db_comment='0 = Above')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_transportations'


class Packages(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    new_name = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    duration = models.ForeignKey(Durations, models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    package_activity = models.ForeignKey(PackageActivities, models.DO_NOTHING, blank=True, null=True)
    package_category = models.ForeignKey(PackageCategories, models.DO_NOTHING, blank=True, null=True)
    day_ijen = models.IntegerField(blank=True, null=True)
    start_destination = models.ForeignKey(Destinations, models.DO_NOTHING, blank=True, null=True)
    end_destination = models.ForeignKey(Destinations, models.DO_NOTHING, related_name='packages_end_destination_set', blank=True, null=True)
    id_url = models.IntegerField(blank=True, null=True)
    package_platform = models.CharField(max_length=255)
    overview = models.TextField()
    meta_description = models.TextField(blank=True, null=True)
    other_information = models.TextField()
    departure = models.TextField(blank=True, null=True)
    return_field = models.TextField(db_column='return', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    review_rating = models.FloatField()
    review_total = models.IntegerField()
    pdf = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField()
    guide_book = models.TextField(blank=True, null=True)
    is_publish = models.CharField(max_length=1)
    b = models.IntegerField()
    l = models.IntegerField()
    d = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    experience = models.ForeignKey(Experiences, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packages'


class Pages(models.Model):
    id = models.BigAutoField(primary_key=True)
    page_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    schema_markup = models.TextField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'


class PasswordActivations(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_activations'


class PasswordResetTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_reset_tokens'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PaymentMethods(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_methods'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class PoliceEscorts(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING, blank=True, null=True)
    start = models.TextField(blank=True, null=True)
    finish = models.TextField(blank=True, null=True)
    departure_time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    police_escort_type = models.CharField(max_length=13, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'police_escorts'


class PosTransfers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    rekening_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_transfers'


class PriceCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    temp_text = models.CharField(max_length=255)
    start = models.IntegerField()
    end = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_categories'


class PriceMakerLocationDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    price_maker = models.ForeignKey('PriceMakers', models.DO_NOTHING, blank=True, null=True)
    price_maker_location = models.ForeignKey('PriceMakerLocations', models.DO_NOTHING, blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    quantity_formula = models.CharField(max_length=255, blank=True, null=True)
    amount_formula = models.CharField(max_length=255, blank=True, null=True)
    pos_transfer = models.ForeignKey(PosTransfers, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_maker_location_details'


class PriceMakerLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    price_maker = models.ForeignKey('PriceMakers', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_maker_locations'


class PriceMakerPricePaxs(models.Model):
    id = models.BigAutoField(primary_key=True)
    price_maker = models.ForeignKey('PriceMakers', models.DO_NOTHING, blank=True, null=True)
    pax = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    hpp_per_pax = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_maker_price_paxs'


class PriceMakers(models.Model):
    id = models.BigAutoField(primary_key=True)
    package_name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    duration = models.ForeignKey(Durations, models.DO_NOTHING, blank=True, null=True)
    is_edit = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_makers'


class PricePlans(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    background = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_plans'


class ReviewGuides(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    guide = models.ForeignKey(GuideDrivers, models.DO_NOTHING)
    star = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_guides'


class Reviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    package = models.ForeignKey(Packages, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    date = models.DateField()
    star = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class RoleUser(models.Model):
    user_id = models.IntegerField()
    role_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role_user'


class RoomHotels(models.Model):
    id = models.BigAutoField(primary_key=True)
    hotel = models.ForeignKey(Hotels, models.DO_NOTHING)
    room_name = models.CharField(max_length=255)
    code = models.IntegerField(blank=True, null=True)
    room_type = models.CharField(max_length=255, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_hotels'


class Services(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class TripExpenseItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    trip_expense_location = models.ForeignKey('TripExpenseLocations', models.DO_NOTHING)
    price_maker_location_detail = models.ForeignKey(PriceMakerLocationDetails, models.DO_NOTHING)
    item = models.CharField(max_length=255)
    rate = models.FloatField()
    quantity = models.FloatField()
    amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_expense_items'


class TripExpenseLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    trip_expense = models.ForeignKey('TripExpenses', models.DO_NOTHING)
    price_maker_location = models.ForeignKey(PriceMakerLocations, models.DO_NOTHING)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_expense_locations'


class TripExpenses(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    price_maker = models.ForeignKey(PriceMakers, models.DO_NOTHING)
    total = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_expenses'


class TwCalculationCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=255)
    no = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_calculation_categories'


class TwCalculationCategoryCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_calculation_category_codes'


class TwCalculationDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    tw_calculation = models.ForeignKey('TwCalculations', models.DO_NOTHING)
    tw_calculation_category = models.ForeignKey(TwCalculationCategories, models.DO_NOTHING)
    tw_calculation_item = models.ForeignKey('TwCalculationItems', models.DO_NOTHING)
    tw_calculation_item_detail = models.ForeignKey('TwCalculationItemDetails', models.DO_NOTHING)
    quantity = models.FloatField()
    rate = models.FloatField()
    amount = models.FloatField()
    is_paid = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_calculation_details'


class TwCalculationItemDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    tw_calculation_item = models.ForeignKey('TwCalculationItems', models.DO_NOTHING)
    pos_transfer = models.ForeignKey(PosTransfers, models.DO_NOTHING, blank=True, null=True)
    no = models.IntegerField()
    agent_code = models.BigIntegerField()
    category_code = models.ForeignKey(TwCalculationCategoryCodes, models.DO_NOTHING, db_column='category_code', blank=True, null=True)
    code = models.BigIntegerField()
    item = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    rate = models.FloatField()
    is_check = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    destination_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_calculation_item_details'


class TwCalculationItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    no = models.IntegerField()
    tw_calculation_category = models.ForeignKey(TwCalculationCategories, models.DO_NOTHING)
    item = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_calculation_items'


class TwCalculations(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING, blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    agent_id = models.PositiveBigIntegerField()
    date_start = models.DateField()
    duration = models.IntegerField(blank=True, null=True)
    pax = models.IntegerField(blank=True, null=True)
    total = models.FloatField()
    paid = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_calculations'


class UserAccommodations(models.Model):
    id = models.BigAutoField(primary_key=True)
    hotel = models.ForeignKey(Hotels, models.DO_NOTHING)
    username = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    fcm_token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_accommodations'


class UserGarages(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    fcm_token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_garages'


class UserJeeps(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    fcm_token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_jeeps'


class UserPartners(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    app_type = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_partners'


class UserPoliceEscorts(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    fcm_token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_police_escorts'


class UserTshirts(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    fcm_token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tshirts'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    google_id = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    referral_code = models.CharField(max_length=255, blank=True, null=True)
    used = models.IntegerField(blank=True, null=True, db_comment='How many the referral code used')
    reward_type = models.CharField(max_length=10, blank=True, null=True)
    reward_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_type = models.CharField(max_length=10, blank=True, null=True, db_comment='discount type for new cust who use the referral code from the referrer')
    discount_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, db_comment='discount amount for new cust who use the referral code from the referrer')
    super = models.IntegerField()
    preferences = models.JSONField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class WaItineraries(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    day = models.IntegerField()
    message = models.TextField()
    guide_book = models.TextField(blank=True, null=True)
    status_guide_book = models.CharField(max_length=2)
    status = models.CharField(max_length=2, db_comment='0:Belum,00:Gagal,1:Sukses')
    schedule = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_itineraries'


class WaLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    message = models.TextField()
    status = models.CharField(max_length=1)
    error = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_logs'


class WeatherCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_codes'


class WebsiteLinkCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_link_categories'


class WebsiteLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    link_category = models.ForeignKey(WebsiteLinkCategories, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    schema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_links'
