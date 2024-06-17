# 
# def get_plot(item_codes, start_datetime=None, end_datetime=None):
#     plt.switch_backend('AGG')
#     plt.figure(figsize=(12, 7))

#     for item_code in item_codes:
#         qs = Sale.objects.filter(item_code=item_code)

#         if start_datetime and end_datetime:
#             qs = qs.filter(temp_time__range=[start_datetime, end_datetime])
#         x = [x.temp_time for x in qs]
#         y = [y.temp_value for y in qs]
#         plt.plot(x, y, label=f'Line {item_code}')

#     plt.xticks(rotation=0)
#     plt.xlabel('------TIME------')
#     plt.ylabel('------ITEM VALUE------')
#     plt.legend()
#     plt.tight_layout()
#     graph = get_graph()
#     return graph

# def get_date_plot(item_code, start_date=None, end_date=None, start_time=None, end_time=None):
#     plt.switch_backend('AGG')
#     plt.figure(figsize=(12, 7))

#     s_date = datetime.strptime(start_date, "%Y-%m-%d").date()
#     e_date = datetime.strptime(end_date, "%Y-%m-%d").date()
#     for delta in range((e_date - s_date).days + 1):
#         current_date = s_date + timedelta(days=delta)

#         start_datetime = datetime.combine(current_date, datetime.strptime(start_time, '%H:%M').time())
#         end_datetime = datetime.combine(current_date, datetime.strptime(end_time, '%H:%M').time())

#         start_datetime = make_aware(start_datetime)  
#         end_datetime = make_aware(end_datetime)  

#         qs = Sale.objects.filter(item_code=item_code, temp_time__range=[start_datetime, end_datetime]).order_by('temp_time')
        
#         x = [(entry.temp_time - start_datetime).total_seconds() / 3600 for entry in qs]
#         x_labels = [start_datetime + timedelta(seconds=x_val * 3600) for x_val in x]
        
#         y = [entry.temp_value for entry in qs]

#         plt.plot(x, y, label=f'{current_date}')

#     plt.xticks(x, [label.strftime('%H:%M') for label in x_labels], rotation=0)
#     plt.xlabel('------TIME (24-Hour)------')
#     plt.ylabel('------ITEM VALUE------')
#     plt.legend()
#     plt.tight_layout()

#     graph = get_graph()
#     return graph



# # def get_date_plot(item_code, start_date=None, end_date=None, start_time=None, end_time=None):
# #     plt.switch_backend('AGG')
# #     plt.figure(figsize=(12, 7))

# #     s_date = datetime.strptime(start_date, "%Y-%m-%d").date()
# #     e_date = datetime.strptime(end_date, "%Y-%m-%d").date()

# #     for delta in range((e_date - s_date).days + 1):
# #         current_date = s_date + timedelta(days=delta)

# #         start_datetime = datetime.combine(current_date, datetime.strptime(start_time, '%H:%M').time())
# #         end_datetime = datetime.combine(current_date, datetime.strptime(end_time, '%H:%M').time())

# #         start_datetime = make_aware(start_datetime)  
# #         end_datetime = make_aware(end_datetime)  

# #         qs = Sale.objects.filter(item_code=item_code, temp_time__range=[start_datetime, end_datetime]).order_by('temp_time')
# #         x = [(entry.temp_time - start_datetime).total_seconds() / 3600 for entry in qs]
# #         y = [entry.temp_value for entry in qs]

# #         plt.plot(x, y, label=f'{current_date}')

# #     plt.xticks(rotation=0)
# #     plt.xlabel('------TIME (24-Hour)------')
# #     plt.ylabel('------ITEM VALUE------')
# #     plt.legend()
# #     plt.tight_layout()

# #     graph = get_graph()
# #     return graph








# # from django.utils.timezone import make_aware
# # def get_date_plot(item_code, start_date=None, end_date=None, start_time=None, end_time=None):
# #     plt.switch_backend('AGG')
# #     plt.figure(figsize=(12, 7))

# #     s_date = datetime.strptime(start_date, "%Y-%m-%d").date()
# #     e_date = datetime.strptime(end_date, "%Y-%m-%d").date()

# #     while s_date <= e_date:
# #         start_datetime = datetime.combine(s_date, datetime.strptime(start_time, '%H:%M').time())
# #         end_datetime = datetime.combine(s_date, datetime.strptime(end_time, '%H:%M').time())
# #         start_datetime = make_aware(start_datetime)  # Convert to aware datetime with timezone
# #         end_datetime = make_aware(end_datetime)  # Convert to aware datetime with timezone
# #         qs = Sale.objects.filter(item_code=item_code, temp_time__range=[start_datetime, end_datetime]).order_by('temp_time')
# #         x = [(entry.temp_time - start_datetime).total_seconds() / 3600 for entry in qs]
# #         y = [entry.temp_value for entry in qs]
# #         plt.plot(x, y, label=f'{s_date}')
# #         s_date += timedelta(days=1)
# #     plt.xticks(rotation=0)
# #     plt.xlabel('------TIME (24-Hour)------')
# #     plt.ylabel('------ITEM VALUE------')
# #     plt.legend()
# #     plt.tight_layout()

# #     graph = get_graph()
# #     return graph




# # def get_date_plot(item_code, start_date=None, end_date=None, start_time=None, end_time=None):
# #     plt.switch_backend('AGG')
# #     plt.figure(figsize=(12, 7))
# #     pdate_array = []
# #     logger.warning("jaisir")
# #     logger.warning(start_date)
# #     logger.warning(end_date)

# #     # dateTimeObj = datetime.strptime(dateString, "%d-%B-%Y")
# #     #s_date= datetime.strptime(start_date, "%Y/%m/%d %H:%M:%S").date()
# #     #e_date= datetime.strptime(end_date, "%Y/%m/%d %H:%M:%S").date()
# #     s_date= datetime.strptime(start_date, "%Y-%m-%d").date()
# #     e_date= datetime.strptime(end_date, "%Y-%m-%d").date()
# #     for delta in range((e_date - s_date).days + 1):
# #         result_date = s_date + timedelta(days=delta)
# #         pdate_array.append(result_date)

# #     for sddate in pdate_array:
# #         qs = Sale.objects.filter(item_code=item_code)

# #         if start_date:
# #             start_datetime = datetime.combine(sddate, datetime.strptime(start_time, '%H:%M').time())
# #             end_datetime = datetime.combine(sddate, datetime.strptime(end_time, '%H:%M').time())

# #         if start_datetime and end_datetime:
# #             qs = qs.filter(temp_time__range=[start_datetime, end_datetime])

# #         x = [x.temp_time for x in qs]
# #         y = [y.temp_value for y in qs]
# #         plt.plot(x, y, label=f'Line {item_code}')

# #     plt.xticks(rotation=0)
# #     plt.xlabel('------TIME------')
# #     plt.ylabel('------ITEM VALUE------')
# #     plt.legend()
# #     plt.tight_layout()
# #     graph = get_graph()
# #     return graph


# # def get_date_plot(item,)


# import mysql.connector
# import random
# from datetime import datetime, timedelta

# # mydb = mysql.connector.connect(
# #  host="localhost",
# #  user="yourusername",
# #  password="yourpassword"
# # )
# # mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE mydatabase")



# # db_config = {
# #     'host': 'localhost',
# #     'user': 'root',
# #     'password': '',
# #     'database': 'BMS_DATA',
# # }
# # battery_codes=['b1','b2','b3','b4','b5']
# # #now = datetime.now()
# # stime = datetime(2023, 12, 20, 10, 0, 0) 
# # connection = mysql.connector.connect(**db_config)
# # cursor = connection.cursor()

# # try:
# #     for battery_code in battery_codes:	
# #         ptime = stime
# #         for i in range(0,24):
# #             ptime =  ptime + timedelta(minutes=15) 
# #             query = "insert into  jove_battery( battery_date,battery_code,process_date, battery_tmp) values (%s,%s,%s,%s)"
# #             print(query)
# #             cursor.execute(query, (ptime,battery_code,ptime,random.uniform(20.5, 35.5),))

# # except mysql.connector.Error as err:
# #     print("Error:", err)
# #     connection.rollback()
# # finally:
# #     connection.commit()














from datetime import datetime, timedelta
# from django.shortcuts import render
# from . models import Sale
# import matplotlib.pyplot as plt
# import base64
# import logging
# from io import BytesIO
# logger = logging.getLogger(__name__)
# from django.utils.timezone import make_aware


# def get_graph():
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     graph = base64.b64encode(image_png)
#     graph = graph.decode('utf-8')
#     buffer.close()
#     return graph

# # <form method="get" id="itemCodeForm">
# #   <select name="item_code" id="itemCodeDropdown" onchange="this.form.submit()">
# #       <option value="" {% if not selected_item_code %}selected{% endif %}>All</option>
# #       {% for item_code in item_codes %}
# #           <option value="{{ item_code }}" {% if item_code == selected_item_code %}selected{% endif %}>{{ item_code }}</option>
# #       {% endfor %}
# #   </select>

# #   <label for="start_date">Start Date:</label>
# #   <input type="date" name="start_date" value="{{ request.GET.start_date }}">
# #   <label for="start_time">Start Time:</label>
# #   <input type="time" name="start_time" value="{{ request.GET.start_time }}">

# #   <label for="end_date">End Date:</label>
# #   <input type="date" name="end_date" value="{{ request.GET.end_date }}">
# #   <label for="end_time">End Time:</label>
# #   <input type="time" name="end_time" value="{{ request.GET.end_time }}">

# #   <input type="submit" value="Filter">
# # </form>
# # {% if chart_all_items %}
# #   <h2>All Items</h2>
# #   <img src="data:image/png;base64, {{ chart_all_items|safe }}" alt="all items graph">
# # {% endif %}

# # {% if chart_selected_item %}
# #   <h2>Selected Item</h2>
# #   <img src="data:image/png;base64, {{ chart_selected_item|safe }}" alt="selected item graph">
# # {% endif %}

# # def home(request):
# #     item_codes = Sale.objects.values_list('item_code', flat=True).distinct()
# #     selected_item_code = request.GET.get('item_code', '')
# #     start_date = request.GET.get('start_date', '')
# #     start_time = request.GET.get('start_time', '')
# #     end_date = request.GET.get('end_date', '')
# #     end_time = request.GET.get('end_time', '')
# #     start_datetime = None
# #     end_datetime = None
# #     if start_date:
# #         start_datetime = datetime.combine(datetime.strptime(start_date, '%Y-%m-%d'), datetime.min.time())
# #         if start_time:
# #             start_datetime += timedelta(hours=datetime.strptime(start_time, '%H:%M').hour,
# #                                         minutes=datetime.strptime(start_time, '%H:%M').minute)
# #     if end_date:
# #         end_datetime = datetime.combine(datetime.strptime(end_date, '%Y-%m-%d'), datetime.min.time())
# #         if end_time:
# #             end_datetime += timedelta(hours=datetime.strptime(end_time, '%H:%M').hour,
# #                                       minutes=datetime.strptime(end_time, '%H:%M').minute)

# #     chart_all_items = get_plot(item_codes, start_datetime, end_datetime)

# #     chart_selected_item = None
# #     if selected_item_code and start_datetime and end_datetime:
# #         chart_selected_item = get_date_plot(selected_item_code, start_date, end_date, start_time, end_time)

# #     return render(request, "shop/index.html", {
# #         'chart_all_items': chart_all_items,
# #         'chart_selected_item': chart_selected_item,
# #         'item_codes': item_codes,
# #         'selected_item_code': selected_item_code,
# #     })
# # from datetime import datetime, timedelta
# # from django.shortcuts import render
# # from . models import Sale
# # import matplotlib.pyplot as plt
# # import base64
# # import logging
# # from io import BytesIO
# # logger = logging.getLogger(__name__)
# # from django.utils.timezone import make_aware


# # def get_graph():
# #     buffer = BytesIO()
# #     plt.savefig(buffer, format='png')
# #     buffer.seek(0)
# #     image_png = buffer.getvalue()
# #     graph = base64.b64encode(image_png)
# #     graph = graph.decode('utf-8')
# #     buffer.close()
# #     return graph

# # def get_plot(item_codes, start_datetime=None, end_datetime=None):
# #     plt.switch_backend('AGG')
# #     plt.figure(figsize=(12, 7))

# #     for item_code in item_codes:
# #         qs = Sale.objects.filter(item_code=item_code)

# #         if start_datetime and end_datetime:
# #             qs = qs.filter(temp_time__range=[start_datetime, end_datetime])
# #         x = [x.temp_time for x in qs]
# #         y = [y.temp_value for y in qs]
# #         plt.plot(x, y, label=f'Line {item_code}')

# #     plt.xticks(rotation=0)
# #     plt.xlabel('------TIME------')
# #     plt.ylabel('------ITEM VALUE------')
# #     plt.legend()
# #     plt.tight_layout()
# #     graph = get_graph()
# #     return graph



# # def get_date_plot(item_code, start_date=None, end_date=None, start_time=None, end_time=None):
# #     plt.switch_backend('AGG')
# #     plt.figure(figsize=(12, 7))

# #     s_date = datetime.strptime(start_date, "%Y-%m-%d").date()
# #     e_date = datetime.strptime(end_date, "%Y-%m-%d").date()

# #     for delta in range((e_date - s_date).days + 1):
# #         current_date = s_date + timedelta(days=delta)

# #         start_datetime = datetime.combine(current_date, datetime.strptime(start_time, '%H:%M').time())
# #         end_datetime = datetime.combine(current_date, datetime.strptime(end_time, '%H:%M').time())

# #         start_datetime = make_aware(start_datetime)  
# #         end_datetime = make_aware(end_datetime)  

# #         qs = Sale.objects.filter(item_code=item_code, temp_time__range=[start_datetime, end_datetime]).order_by('temp_time')
# #         x = [(entry.temp_time - start_datetime).total_seconds() / 3600 for entry in qs]
# #         y = [entry.temp_value for entry in qs]

# #         plt.plot(x, y, label=f'{current_date}')

# #     plt.xticks(rotation=0)
# #     plt.xlabel('------TIME (24-Hour)------')
# #     plt.ylabel('------ITEM VALUE------')
# #     plt.legend()
# #     plt.tight_layout()

# #     graph = get_graph()
# #     return graph




# # def get_date_plot(item_code, start_date=None, end_date=None, start_time=None, end_time=None):
# #     plt.switch_backend('AGG')
# #     plt.figure(figsize=(12, 7))
# #     pdate_array = []
# #     logger.warning("jaisir")
# #     logger.warning(start_date)
# #     logger.warning(end_date)

# #     # dateTimeObj = datetime.strptime(dateString, "%d-%B-%Y")
# #     #s_date= datetime.strptime(start_date, "%Y/%m/%d %H:%M:%S").date()
# #     #e_date= datetime.strptime(end_date, "%Y/%m/%d %H:%M:%S").date()
# #     s_date= datetime.strptime(start_date, "%Y-%m-%d").date()
# #     e_date= datetime.strptime(end_date, "%Y-%m-%d").date()
# #     for delta in range((e_date - s_date).days + 1):
# #         result_date = s_date + timedelta(days=delta)
# #         logger.warning("jaisir")
# #         logger.warning(result_date)
# #         pdate_array.append(result_date)

# #     for sddate in pdate_array:
# #         qs = Sale.objects.filter(item_code=item_code)

# #         if start_date:
# #             start_datetime = datetime.combine(sddate, datetime.strptime(start_time, '%H:%M').time())
# #             end_datetime = datetime.combine(sddate, datetime.strptime(end_time, '%H:%M').time())

# #         if start_datetime and end_datetime:
# #             qs = qs.filter(temp_time__range=[start_datetime, end_datetime])

# #         x = [x.temp_time for x in qs]
# #         y = [y.temp_value for y in qs]
# #         plt.plot(x, y, label=f'Line {item_code}')

# #     plt.xticks(rotation=0)
# #     plt.xlabel('------TIME------')
# #     plt.ylabel('------ITEM VALUE------')
# #     plt.legend()
# #     plt.tight_layout()
# #     graph = get_graph()
# #     return graph# views.py

from django.shortcuts import render
from .models import Sale
from .forms import ItemCodeForm
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(item_codes, start_datetime=None, end_datetime=None):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 7))

    for item_code in item_codes:
        qs = Sale.objects.filter(item_code=item_code)

        if start_datetime and end_datetime:
            qs = qs.filter(temp_time__range=[start_datetime, end_datetime])
        x = [x.temp_time for x in qs]
        y = [y.temp_value for y in qs]
        plt.plot(x, y, label=f'Line {item_code}')

    plt.xticks(rotation=0)
    plt.xlabel('------TIME------')
    plt.ylabel('------ITEM VALUE------')
    plt.legend()
    plt.tight_layout()
    
    graph = get_graph()
    return graph
def get_date_plot(item_code, start_date=None, end_date=None, start_time=None, end_time=None):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 7))

    s_date = start_date
    e_date = end_date

    for delta in range((e_date - s_date).days + 1):
        current_date = s_date + timedelta(days=delta)

        start_datetime = datetime.combine(current_date, start_time)
        end_datetime = datetime.combine(current_date, end_time)

        start_datetime = make_aware(start_datetime)
        end_datetime = make_aware(end_datetime)

        qs = Sale.objects.filter(item_code=item_code, temp_time__range=[start_datetime, end_datetime]).order_by('temp_time')

        x = [(entry.temp_time - start_datetime).total_seconds() / 3600 for entry in qs]
        x_labels = [start_datetime + timedelta(seconds=x_val * 3600) for x_val in x]

        y = [entry.temp_value for entry in qs]

        plt.plot(x, y, label=f'{current_date}')

    # Select 8 evenly spaced x-ticks
    x_ticks_indices = np.linspace(0, len(x_labels) - 1, 8, dtype=int)
    selected_x_labels = [x_labels[i] for i in x_ticks_indices]
    selected_x_ticks = [(label - selected_x_labels[0]).total_seconds() / 3600 for label in selected_x_labels]

    plt.xticks(selected_x_ticks, [label.strftime('%H:%M') for label in selected_x_labels], rotation=0)

    plt.xlabel('------TIME (24-Hour)------')
    plt.ylabel('------ITEM VALUE------')
    plt.legend()
    plt.tight_layout()

    graph = get_graph()
    return graph
import numpy as np

