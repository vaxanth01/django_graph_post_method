import numpy as np
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

