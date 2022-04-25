export default {
    authHeader() {
        let accessToken = localStorage.getItem("jwt");

        if (accessToken) {
            return { Authorization: "Bearer " + accessToken };
        } else {
            return {};
        }
    }
}