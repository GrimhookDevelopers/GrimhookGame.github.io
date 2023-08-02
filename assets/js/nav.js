if (window.addEventListener)
{
    window.addEventListener('load', setupAutoHighlight);
}
else
{
    window.attachEvent('onload', setupAutoHighlight);
}

function setupAutoHighlight()
{
    let nav = document.getElementsByTagName("nav")[0];
    let navHeaders = nav.getElementsByTagName("a");
    let anchors = [];

    // find each links header in the page
    for (const header of navHeaders)
    {
        if (!header.hash) continue;
        let anchor = document.getElementById(header.hash.slice(1));
        anchors.push(anchor);
    }

    // make sure the headers are sorted
    anchors.sort(function(a, b)
    {
        return b.offsetTop - a.offsetTop;
    });

    // hookup event
    document.addEventListener('scroll', (e) =>
    {
        highlight(navHeaders, anchors)
    });
    // go ahead and run at startup too
    highlight(navHeaders, anchors)
}

function highlight(headers, anchors)
{
    let scroll = this.scrollY;
    let minHeight = scroll + 300;

    // figure out which anchor on the page should be active
    let activeAnchor = null;
    for (const anchor of anchors)
    {
        if (anchor.offsetTop > minHeight) continue;

        activeAnchor = anchor;
        break;
    }

    if (activeAnchor == null)
    {
        console.error("Unable to find an active anchor.");
        return;
    }

    // update the headers
    for (const header of headers)
    {
        if (header.hash.slice(1) == activeAnchor.id)
        {
            header.classList.add("active");
        }
        else
        {
            header.classList.remove("active");
        }
    }
}
