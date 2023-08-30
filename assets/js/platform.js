function detectPlatform()
{
    if (navigator.userAgent.indexOf("Win") != -1)
    {
        return "Windows";
    }    
    if (navigator.userAgent.indexOf("Mac") != -1)
    {
        return "Mac";
    }    
    if (navigator.userAgent.indexOf("Linux") != -1)
    {
        return "Linux";
    }    
    if (navigator.userAgent.indexOf("Android") != -1)
    {
        return "Android";
    }    
    if (navigator.userAgent.indexOf("like Mac") != -1)
    {
        return "ios";
    }    

    return "Unknown";
}

function setElementsVisibility(style, className, active)
{
    style.innerHTML += `.${className} { display: ${active ? 'inherit' : 'none' } !important; }`;
}

// this will run immediately to prevent platform specific content from shifting
const styleroot = document.createElement("style");

if (detectPlatform() === "Windows")
{
    setElementsVisibility(styleroot, "hide-on-windows", false)
}
else
{
    setElementsVisibility(styleroot, "hide-on-not-windows", false)
}

document.head.appendChild(styleroot);
