import { BotMessage } from "@/components/stocks";
import { nanoid } from "nanoid";

export function useModelAction() {
    async function submitUserMessage(message: string) {
        const response = await fetch("https://shortly-heroic-owl.ngrok-free.app/api/chat?question=" + message, {
            headers: {
                "ngrok-skip-browser-warning": "yes",
            }
        },);
        const responseMessage = await response.text();
        return {
            id: nanoid(),
            display: <BotMessage content={responseMessage} />
        }
    }
    return { submitUserMessage };
}