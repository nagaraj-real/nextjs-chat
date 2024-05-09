import { BotMessage } from "@/components/stocks";
import { nanoid } from "nanoid";

export function useModelAction() {
    async function submitUserMessage(message: string) {
        const response = await fetch("/api/chat?question=" + message);
        const responseMessage = await response.text();
        return {
            id: nanoid(),
            display: <BotMessage content={responseMessage} />
        }
    }
    return { submitUserMessage };
}