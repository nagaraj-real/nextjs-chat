import { NextResponse } from 'next/server';

export default async function middleware() {
  // Continue processing the request
  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)']
}
