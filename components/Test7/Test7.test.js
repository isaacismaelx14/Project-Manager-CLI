import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test7 from "./";
describe("<Test7 />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test7 />);
  });
  test("should render", () => {
    component.getByText("Test7");
  });
});