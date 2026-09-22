from django.shortcuts import get_object_or_404, render
from .models import Event
from polls.models import Poll

def event_list(request):
    events = Event.objects.all()

    return render(
        request,
        "events/event_list.html",
        {"events": events}
    )


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    poll = Poll.objects.filter(event=event).first()

    if request.method == "POST":
        choice_id = request.POST.get("choice")

        if choice_id:
            choice = get_object_or_404(
                poll.choice_set,
                id=choice_id
            )

            choice.votes += 1
            choice.save()

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "poll": poll,
        }
    )

def event_results(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    poll = Poll.objects.filter(event=event).first()

    total_votes = 0

    if poll:
        total_votes = sum(
            choice.votes
            for choice in poll.choice_set.all()
        )

    return render(
        request,
        "events/event_results.html",
        {
            "event": event,
            "poll": poll,
            "total_votes": total_votes,
        }
    )