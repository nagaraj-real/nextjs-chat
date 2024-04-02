
export function EmptyScreen() {
  return (
    <div className="mx-auto max-w-2xl px-4">
      <div className="flex flex-col gap-2 rounded-lg border bg-background p-8">
        <h1 className="text-lg font-semibold">
          Welcome to Nagarajan's Resume AI Chatbot!
        </h1>
        <p className="leading-normal text-muted-foreground">
          The chatbot can answer any questions related to my resume.
          It can also have general conversation and help with any queries.
        </p>
      </div>
    </div>
  )
}
