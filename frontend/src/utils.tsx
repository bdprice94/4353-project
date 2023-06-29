export const backendurl = "http://localhost:8000/api"; // will need to read from env if we need to host this

export function setCookie(name: string, val: string) {
    const date = new Date();

    date.setTime(date.getTime() + (7 * 24 * 60 * 60 * 1000))
    document.cookie = `${name}=${val}; expires=${date.toUTCString()}; path=/`
}

export function getCookie(name: string) {
    const value = `; ${document.cookie}`
    const parts = value.split(`; ${name}=`)

    if (parts.length == 2) {
        // @ts-ignore
        return parts.pop().split(";").shift();
    }
}
